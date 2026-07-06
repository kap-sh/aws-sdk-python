"""Generated from Smithy shape ``com.amazonaws.connect#StartContactMediaProcessingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.contact_media_processing_failure_mode
    import aws_sdk_connect.types.instance_id


class StartContactMediaProcessingRequest(TypedDict, closed=True):
    instance_id: NotRequired["aws_sdk_connect.types.instance_id.InstanceId"]
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: NotRequired["aws_sdk_connect.types.contact_id.ContactId"]
    """<p>The identifier of the contact.</p>"""
    processor_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p> The Amazon Resource Name (ARN) of the Lambda processor. You can find the Amazon Resource Name of the lambda in the lambda console. </p>"""
    failure_mode: NotRequired[
        "aws_sdk_connect.types.contact_media_processing_failure_mode.ContactMediaProcessingFailureMode"
    ]
    """<p> The desired behavior for failed message processing. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartContactMediaProcessingRequest) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    if "processor_arn" in value:
        out["ProcessorArn"] = value["processor_arn"]
    if "failure_mode" in value:
        import aws_sdk_connect.types.contact_media_processing_failure_mode

        out["FailureMode"] = (
            aws_sdk_connect.types.contact_media_processing_failure_mode.serialize_json(
                value["failure_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartContactMediaProcessingRequest:
    out: StartContactMediaProcessingRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    if "ProcessorArn" in data:
        out["processor_arn"] = data["ProcessorArn"]
    if "FailureMode" in data:
        import aws_sdk_connect.types.contact_media_processing_failure_mode

        out["failure_mode"] = (
            aws_sdk_connect.types.contact_media_processing_failure_mode.deserialize_json(
                data["FailureMode"]
            )
        )
    return out
