"""Generated from Smithy shape ``com.amazonaws.mturk#CreateQualificationTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mturk.types.boolean
    import aws_sdk_mturk.types.integer
    import aws_sdk_mturk.types.long
    import aws_sdk_mturk.types.qualification_type_status
    import aws_sdk_mturk.types.string


class CreateQualificationTypeRequest(TypedDict):
    name: "aws_sdk_mturk.types.string.String"
    """<p> The name you give to the Qualification type. The type name is used to represent the Qualification to Workers, and to find the type using a Qualification type search. It must be unique across all of your Qualification types.</p>"""
    keywords: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p>One or more words or phrases that describe the Qualification type, separated by commas. The keywords of a type make the type easier to find during a search.</p>"""
    description: "aws_sdk_mturk.types.string.String"
    """<p>A long description for the Qualification type. On the Amazon Mechanical Turk website, the long description is displayed when a Worker examines a Qualification type.</p>"""
    qualification_type_status: (
        "aws_sdk_mturk.types.qualification_type_status.QualificationTypeStatus"
    )
    """<p>The initial status of the Qualification type.</p> <p>Constraints: Valid values are: Active | Inactive</p>"""
    retry_delay_in_seconds: NotRequired["aws_sdk_mturk.types.long.Long"]
    """<p>The number of seconds that a Worker must wait after requesting a Qualification of the Qualification type before the worker can retry the Qualification request.</p> <p>Constraints: None. If not specified, retries are disabled and Workers can request a Qualification of this type only once, even if the Worker has not been granted the Qualification. It is not possible to disable retries for a Qualification type after it has been created with retries enabled. If you want to disable retries, you must delete existing retry-enabled Qualification type and then create a new Qualification type with retries disabled.</p>"""
    test: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> The questions for the Qualification test a Worker must answer correctly to obtain a Qualification of this type. If this parameter is specified, <code>TestDurationInSeconds</code> must also be specified. </p> <p>Constraints: Must not be longer than 65535 bytes. Must be a QuestionForm data structure. This parameter cannot be specified if AutoGranted is true.</p> <p>Constraints: None. If not specified, the Worker may request the Qualification without answering any questions.</p>"""
    answer_key: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p>The answers to the Qualification test specified in the Test parameter, in the form of an AnswerKey data structure.</p> <p>Constraints: Must not be longer than 65535 bytes.</p> <p>Constraints: None. If not specified, you must process Qualification requests manually.</p>"""
    test_duration_in_seconds: NotRequired["aws_sdk_mturk.types.long.Long"]
    """<p>The number of seconds the Worker has to complete the Qualification test, starting from the time the Worker requests the Qualification.</p>"""
    auto_granted: NotRequired["aws_sdk_mturk.types.boolean.Boolean"]
    """<p>Specifies whether requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test.</p> <p>Constraints: If the Test parameter is specified, this parameter cannot be true.</p>"""
    auto_granted_value: NotRequired["aws_sdk_mturk.types.integer.Integer"]
    """<p>The Qualification value to use for automatically granted Qualifications. This parameter is used only if the AutoGranted parameter is true.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateQualificationTypeRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "keywords" in value:
        out["Keywords"] = value["keywords"]
    out["Description"] = value["description"]
    import aws_sdk_mturk.types.qualification_type_status

    out["QualificationTypeStatus"] = (
        aws_sdk_mturk.types.qualification_type_status.serialize_aws_json_1_1(
            value["qualification_type_status"]
        )
    )
    if "retry_delay_in_seconds" in value:
        out["RetryDelayInSeconds"] = value["retry_delay_in_seconds"]
    if "test" in value:
        out["Test"] = value["test"]
    if "answer_key" in value:
        out["AnswerKey"] = value["answer_key"]
    if "test_duration_in_seconds" in value:
        out["TestDurationInSeconds"] = value["test_duration_in_seconds"]
    if "auto_granted" in value:
        out["AutoGranted"] = value["auto_granted"]
    if "auto_granted_value" in value:
        out["AutoGrantedValue"] = value["auto_granted_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateQualificationTypeRequest:
    out: CreateQualificationTypeRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateQualificationTypeRequest.name required")
    if "Keywords" in data:
        out["keywords"] = data["Keywords"]
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError(
            "CreateQualificationTypeRequest.description required"
        )
    if "QualificationTypeStatus" in data:
        import aws_sdk_mturk.types.qualification_type_status

        out["qualification_type_status"] = (
            aws_sdk_mturk.types.qualification_type_status.deserialize_aws_json_1_1(
                data["QualificationTypeStatus"]
            )
        )
    else:
        raise DeserializationError(
            "CreateQualificationTypeRequest.qualification_type_status required"
        )
    if "RetryDelayInSeconds" in data:
        out["retry_delay_in_seconds"] = data["RetryDelayInSeconds"]
    if "Test" in data:
        out["test"] = data["Test"]
    if "AnswerKey" in data:
        out["answer_key"] = data["AnswerKey"]
    if "TestDurationInSeconds" in data:
        out["test_duration_in_seconds"] = data["TestDurationInSeconds"]
    if "AutoGranted" in data:
        out["auto_granted"] = data["AutoGranted"]
    if "AutoGrantedValue" in data:
        out["auto_granted_value"] = data["AutoGrantedValue"]
    return out
