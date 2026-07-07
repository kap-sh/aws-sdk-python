"""Generated from Smithy shape ``com.amazonaws.mturk#QualificationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mturk.types.boolean
    import aws_sdk_mturk.types.entity_id
    import aws_sdk_mturk.types.integer
    import aws_sdk_mturk.types.long
    import aws_sdk_mturk.types.qualification_type_status
    import aws_sdk_mturk.types.string
    import aws_sdk_mturk.types.timestamp


class QualificationType(TypedDict, closed=True):
    qualification_type_id: NotRequired["aws_sdk_mturk.types.entity_id.EntityId"]
    """<p> A unique identifier for the Qualification type. A Qualification type is given a Qualification type ID when you call the CreateQualificationType operation. </p>"""
    creation_time: NotRequired["aws_sdk_mturk.types.timestamp.Timestamp"]
    """<p> The date and time the Qualification type was created. </p>"""
    name: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> The name of the Qualification type. The type name is used to identify the type, and to find the type using a Qualification type search. </p>"""
    description: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> A long description for the Qualification type. </p>"""
    keywords: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> One or more words or phrases that describe theQualification type, separated by commas. The Keywords make the type easier to find using a search. </p>"""
    qualification_type_status: NotRequired[
        "aws_sdk_mturk.types.qualification_type_status.QualificationTypeStatus"
    ]
    """<p> The status of the Qualification type. A Qualification type's status determines if users can apply to receive a Qualification of this type, and if HITs can be created with requirements based on this type. Valid values are Active | Inactive. </p>"""
    test: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> The questions for a Qualification test associated with this Qualification type that a user can take to obtain a Qualification of this type. This parameter must be specified if AnswerKey is present. A Qualification type cannot have both a specified Test parameter and an AutoGranted value of true. </p>"""
    test_duration_in_seconds: NotRequired["aws_sdk_mturk.types.long.Long"]
    """<p> The amount of time, in seconds, given to a Worker to complete the Qualification test, beginning from the time the Worker requests the Qualification. </p>"""
    answer_key: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p>The answers to the Qualification test specified in the Test parameter.</p>"""
    retry_delay_in_seconds: NotRequired["aws_sdk_mturk.types.long.Long"]
    """<p> The amount of time, in seconds, Workers must wait after taking the Qualification test before they can take it again. Workers can take a Qualification test multiple times if they were not granted the Qualification from a previous attempt, or if the test offers a gradient score and they want a better score. If not specified, retries are disabled and Workers can request a Qualification only once. </p>"""
    is_requestable: NotRequired["aws_sdk_mturk.types.boolean.Boolean"]
    """<p> Specifies whether the Qualification type is one that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test. This value is False for Qualifications assigned automatically by the system. Valid values are True | False. </p>"""
    auto_granted: NotRequired["aws_sdk_mturk.types.boolean.Boolean"]
    """<p>Specifies that requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test. Valid values are True | False.</p>"""
    auto_granted_value: NotRequired["aws_sdk_mturk.types.integer.Integer"]
    """<p> The Qualification integer value to use for automatically granted Qualifications, if AutoGranted is true. This is 1 by default. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QualificationType) -> dict:
    out: dict = {}
    if "qualification_type_id" in value:
        out["QualificationTypeId"] = value["qualification_type_id"]
    if "creation_time" in value:
        import aws_sdk_mturk.types.timestamp

        out["CreationTime"] = aws_sdk_mturk.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "keywords" in value:
        out["Keywords"] = value["keywords"]
    if "qualification_type_status" in value:
        import aws_sdk_mturk.types.qualification_type_status

        out["QualificationTypeStatus"] = (
            aws_sdk_mturk.types.qualification_type_status.serialize_aws_json_1_1(
                value["qualification_type_status"]
            )
        )
    if "test" in value:
        out["Test"] = value["test"]
    if "test_duration_in_seconds" in value:
        out["TestDurationInSeconds"] = value["test_duration_in_seconds"]
    if "answer_key" in value:
        out["AnswerKey"] = value["answer_key"]
    if "retry_delay_in_seconds" in value:
        out["RetryDelayInSeconds"] = value["retry_delay_in_seconds"]
    if "is_requestable" in value:
        out["IsRequestable"] = value["is_requestable"]
    if "auto_granted" in value:
        out["AutoGranted"] = value["auto_granted"]
    if "auto_granted_value" in value:
        out["AutoGrantedValue"] = value["auto_granted_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QualificationType:
    out: QualificationType = {}  # type: ignore[typeddict-item]
    if "QualificationTypeId" in data:
        out["qualification_type_id"] = data["QualificationTypeId"]
    if "CreationTime" in data:
        import aws_sdk_mturk.types.timestamp

        out["creation_time"] = aws_sdk_mturk.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Keywords" in data:
        out["keywords"] = data["Keywords"]
    if "QualificationTypeStatus" in data:
        import aws_sdk_mturk.types.qualification_type_status

        out["qualification_type_status"] = (
            aws_sdk_mturk.types.qualification_type_status.deserialize_aws_json_1_1(
                data["QualificationTypeStatus"]
            )
        )
    if "Test" in data:
        out["test"] = data["Test"]
    if "TestDurationInSeconds" in data:
        out["test_duration_in_seconds"] = data["TestDurationInSeconds"]
    if "AnswerKey" in data:
        out["answer_key"] = data["AnswerKey"]
    if "RetryDelayInSeconds" in data:
        out["retry_delay_in_seconds"] = data["RetryDelayInSeconds"]
    if "IsRequestable" in data:
        out["is_requestable"] = data["IsRequestable"]
    if "AutoGranted" in data:
        out["auto_granted"] = data["AutoGranted"]
    if "AutoGrantedValue" in data:
        out["auto_granted_value"] = data["AutoGrantedValue"]
    return out
