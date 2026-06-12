"""Generated from Smithy shape ``com.amazonaws.mturk#QualificationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mturk.types.customer_id
    import aws_sdk_mturk.types.entity_id
    import aws_sdk_mturk.types.string
    import aws_sdk_mturk.types.timestamp


class QualificationRequest(TypedDict):
    qualification_request_id: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p>The ID of the Qualification request, a unique identifier generated when the request was submitted. </p>"""
    qualification_type_id: NotRequired["aws_sdk_mturk.types.entity_id.EntityId"]
    """<p> The ID of the Qualification type the Worker is requesting, as returned by the CreateQualificationType operation. </p>"""
    worker_id: NotRequired["aws_sdk_mturk.types.customer_id.CustomerId"]
    """<p> The ID of the Worker requesting the Qualification.</p>"""
    test: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> The contents of the Qualification test that was presented to the Worker, if the type has a test and the Worker has submitted answers. This value is identical to the QuestionForm associated with the Qualification type at the time the Worker requests the Qualification.</p>"""
    answer: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> The Worker's answers for the Qualification type's test contained in a QuestionFormAnswers document, if the type has a test and the Worker has submitted answers. If the Worker does not provide any answers, Answer may be empty. </p>"""
    submit_time: NotRequired["aws_sdk_mturk.types.timestamp.Timestamp"]
    """<p>The date and time the Qualification request had a status of Submitted. This is either the time the Worker submitted answers for a Qualification test, or the time the Worker requested the Qualification if the Qualification type does not have a test. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QualificationRequest) -> dict:
    out: dict = {}
    if "qualification_request_id" in value:
        out["QualificationRequestId"] = value["qualification_request_id"]
    if "qualification_type_id" in value:
        out["QualificationTypeId"] = value["qualification_type_id"]
    if "worker_id" in value:
        out["WorkerId"] = value["worker_id"]
    if "test" in value:
        out["Test"] = value["test"]
    if "answer" in value:
        out["Answer"] = value["answer"]
    if "submit_time" in value:
        import aws_sdk_mturk.types.timestamp

        out["SubmitTime"] = aws_sdk_mturk.types.timestamp.serialize_aws_json_1_1(
            value["submit_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QualificationRequest:
    out: QualificationRequest = {}  # type: ignore[typeddict-item]
    if "QualificationRequestId" in data:
        out["qualification_request_id"] = data["QualificationRequestId"]
    if "QualificationTypeId" in data:
        out["qualification_type_id"] = data["QualificationTypeId"]
    if "WorkerId" in data:
        out["worker_id"] = data["WorkerId"]
    if "Test" in data:
        out["test"] = data["Test"]
    if "Answer" in data:
        out["answer"] = data["Answer"]
    if "SubmitTime" in data:
        import aws_sdk_mturk.types.timestamp

        out["submit_time"] = aws_sdk_mturk.types.timestamp.deserialize_aws_json_1_1(
            data["SubmitTime"]
        )
    return out
