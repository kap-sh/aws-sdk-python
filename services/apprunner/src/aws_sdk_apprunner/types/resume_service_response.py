"""Generated from Smithy shape ``com.amazonaws.apprunner#ResumeServiceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.service
    import aws_sdk_apprunner.types.uuid


class ResumeServiceResponse(TypedDict):
    service: "aws_sdk_apprunner.types.service.Service"
    """<p>A description of the App Runner service that this request just resumed.</p>"""
    operation_id: NotRequired["aws_sdk_apprunner.types.uuid.UUID"]
    """<p>The unique ID of the asynchronous operation that this request started. You can use it combined with the <a>ListOperations</a> call to track the operation's progress.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResumeServiceResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.service

    out["Service"] = aws_sdk_apprunner.types.service.serialize_aws_json_1_0(
        value["service"]
    )
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResumeServiceResponse:
    out: ResumeServiceResponse = {}  # type: ignore[typeddict-item]
    if "Service" in data:
        import aws_sdk_apprunner.types.service

        out["service"] = aws_sdk_apprunner.types.service.deserialize_aws_json_1_0(
            data["Service"]
        )
    else:
        raise DeserializationError("ResumeServiceResponse.service required")
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    return out
