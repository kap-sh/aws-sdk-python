"""Generated from Smithy shape ``com.amazonaws.apprunner#UpdateServiceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.service
    import aws_sdk_apprunner.types.uuid


class UpdateServiceResponse(TypedDict):
    service: "aws_sdk_apprunner.types.service.Service"
    """<p>A description of the App Runner service updated by this request. All configuration values in the returned <code>Service</code> structure reflect configuration changes that are being applied by this request.</p>"""
    operation_id: "aws_sdk_apprunner.types.uuid.UUID"
    """<p>The unique ID of the asynchronous operation that this request started. You can use it combined with the <a>ListOperations</a> call to track the operation's progress.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.service

    out["Service"] = aws_sdk_apprunner.types.service.serialize_aws_json_1_0(
        value["service"]
    )
    out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceResponse:
    out: UpdateServiceResponse = {}  # type: ignore[typeddict-item]
    if "Service" in data:
        import aws_sdk_apprunner.types.service

        out["service"] = aws_sdk_apprunner.types.service.deserialize_aws_json_1_0(
            data["Service"]
        )
    else:
        raise DeserializationError("UpdateServiceResponse.service required")
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    else:
        raise DeserializationError("UpdateServiceResponse.operation_id required")
    return out
