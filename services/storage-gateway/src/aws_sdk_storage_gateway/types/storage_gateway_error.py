"""Generated from Smithy shape ``com.amazonaws.storagegateway#StorageGatewayError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.error_code
    import aws_sdk_storage_gateway.types.error_details


class StorageGatewayError(TypedDict):
    error_code: NotRequired["aws_sdk_storage_gateway.types.error_code.ErrorCode"]
    """<p>Additional information about the error.</p>"""
    error_details: NotRequired[
        "aws_sdk_storage_gateway.types.error_details.errorDetails"
    ]
    """<p>Human-readable text that provides detail about the error that occurred.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageGatewayError) -> dict:
    out: dict = {}
    if "error_code" in value:
        import aws_sdk_storage_gateway.types.error_code

        out["errorCode"] = (
            aws_sdk_storage_gateway.types.error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_details" in value:
        import aws_sdk_storage_gateway.types.error_details

        out["errorDetails"] = (
            aws_sdk_storage_gateway.types.error_details.serialize_aws_json_1_1(
                value["error_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StorageGatewayError:
    out: StorageGatewayError = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        import aws_sdk_storage_gateway.types.error_code

        out["error_code"] = (
            aws_sdk_storage_gateway.types.error_code.deserialize_aws_json_1_1(
                data["errorCode"]
            )
        )
    if "errorDetails" in data:
        import aws_sdk_storage_gateway.types.error_details

        out["error_details"] = (
            aws_sdk_storage_gateway.types.error_details.deserialize_aws_json_1_1(
                data["errorDetails"]
            )
        )
    return out
