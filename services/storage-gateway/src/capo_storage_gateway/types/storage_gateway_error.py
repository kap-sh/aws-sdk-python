"""Generated from Smithy shape ``com.amazonaws.storagegateway#StorageGatewayError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.error_code
    import capo_storage_gateway.types.error_details


class StorageGatewayError(TypedDict, closed=True):
    error_code: NotRequired["capo_storage_gateway.types.error_code.ErrorCode"]
    """<p>Additional information about the error.</p>"""
    error_details: NotRequired["capo_storage_gateway.types.error_details.errorDetails"]
    """<p>Human-readable text that provides detail about the error that occurred.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageGatewayError) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_storage_gateway.types.error_code

        out["errorCode"] = capo_storage_gateway.types.error_code.serialize_aws_json_1_1(
            value["error_code"]
        )
    if "error_details" in value:
        import capo_storage_gateway.types.error_details

        out["errorDetails"] = (
            capo_storage_gateway.types.error_details.serialize_aws_json_1_1(
                value["error_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StorageGatewayError:
    out: StorageGatewayError = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        import capo_storage_gateway.types.error_code

        out["error_code"] = (
            capo_storage_gateway.types.error_code.deserialize_aws_json_1_1(
                data["errorCode"]
            )
        )
    if "errorDetails" in data:
        import capo_storage_gateway.types.error_details

        out["error_details"] = (
            capo_storage_gateway.types.error_details.deserialize_aws_json_1_1(
                data["errorDetails"]
            )
        )
    return out
