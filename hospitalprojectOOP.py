class Patient:
    def __init__(self,name,ailment,age,patient_id):
        self.name=name
        self.ailment=ailment
        self.age=age
        self.patient_id=patient_id
        self.doctor_assigned=None
        self.treatment_plan=[]
    def view_details(self):
        doctor_info=self.doctor_assigned.name if self.doctor_assigned else "No doctor assigned"
        return f"patient id:{self.patient_id} - name: {self.name} - ailment: {self.ailment} - doctor assigned: {self.doctor_assigned} - treatment plan: {self.treatment_plan}"
    def add_treatment(self,treatment):
        self.treatment_plan.append(treatment)
        return f"treatment: {treatment} added"
    def assign_doctor(self,doctor):
        self.assign_doctor=doctor
        return f"doctor {doctor} assigned"
class Doctor:
    def __init__(self,doctor_id,name,specialization):
        self.name=name
        self.doctor_id=doctor_id
        self.specialization=specialization
        self.patient_list=[]
    def view_details(self):
        return f"doctor name: {self.name} - doctor id: {self.doctor_id} - specialization: {self.specialization}"
    def assign_patient(self,patient):
        self.patient_list.append(patient)
        return f"patient: {patient.name} assigned"
class Hospital:
    def __init__(self):
        self.doctors=[]
        self.patients=[]
    def add_patient(self,patient):
        self.patients.append(patient)
        return f"patient: {patient} added"
    def add_doctor(self,doctor):
        self.doctors.append(doctor)
        return f"doctor: {doctor} added"
    def assign_doctor_to_pateint(self,patient_id,doctor_id):
        doctor=next((doc for doc in self.doctors if doc.doctor_id==doctor_id),None)
        patient=next((pat for pat in self.patients if pat.patient_id==patient_id))
        if doctor and patient:
            doctor.assign_patient=doctor    
            patient.assign_doctor=patient
            return f"doctor {doctor} assigned to the patient {patient}"
        else:
            return "nothing found"
    def view_all_patients(self):
        return [patient.view_details() for patient in self.patients]
    def view_all_doctors(self):
        return [doctor.view_details() for doctor in self.doctors]
if __name__=="__main__":
    hospital=Hospital()
    doctor1=Doctor("Dr.Aimal","Cardiology",1)
    doctor2=Doctor("Dr.Maryam","Neurologist",2)
    patient1=Patient("Umair","Loving Heart",20,111)
    patient2=Patient("Ali","Loving Heart",21,112)
    patient1.add_treatment("Love")
    patient2.add_treatment("Love")
    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)
    hospital.add_patient(patient1)
    hospital.add_patient(patient2)
    hospital.assign_doctor_to_pateint(111,1)
    hospital.assign_doctor_to_pateint(112,2)
    patient1.add_treatment("Love")
    patient2.add_treatment("Love")
    print("/n All patient details: ")
    for detail in hospital.view_all_patients():
        print(detail)
    for detail in hospital.view_all_doctors():
        print(detail)