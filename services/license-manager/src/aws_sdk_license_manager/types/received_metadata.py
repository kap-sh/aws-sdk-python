"""Generated from Smithy shape ``com.amazonaws.licensemanager#ReceivedMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.allowed_operation_list
    import aws_sdk_license_manager.types.received_status
    import aws_sdk_license_manager.types.status_reason_message


class ReceivedMetadata(TypedDict):
    received_status: NotRequired[
        "aws_sdk_license_manager.types.received_status.ReceivedStatus"
    ]
    """<p>Received status.</p>"""
    received_status_reason: NotRequired[
        "aws_sdk_license_manager.types.status_reason_message.StatusReasonMessage"
    ]
    """<p>Received status reason.</p>"""
    allowed_operations: NotRequired[
        "aws_sdk_license_manager.types.allowed_operation_list.AllowedOperationList"
    ]
    """<p>Allowed operations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReceivedMetadata) -> dict:
    out: dict = {}
    if "received_status" in value:
        import aws_sdk_license_manager.types.received_status

        out["ReceivedStatus"] = (
            aws_sdk_license_manager.types.received_status.serialize_aws_json_1_1(
                value["received_status"]
            )
        )
    if "received_status_reason" in value:
        out["ReceivedStatusReason"] = value["received_status_reason"]
    if "allowed_operations" in value:
        import aws_sdk_license_manager.types.allowed_operation_list

        out["AllowedOperations"] = (
            aws_sdk_license_manager.types.allowed_operation_list.serialize_aws_json_1_1(
                value["allowed_operations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReceivedMetadata:
    out: ReceivedMetadata = {}  # type: ignore[typeddict-item]
    if "ReceivedStatus" in data:
        import aws_sdk_license_manager.types.received_status

        out["received_status"] = (
            aws_sdk_license_manager.types.received_status.deserialize_aws_json_1_1(
                data["ReceivedStatus"]
            )
        )
    if "ReceivedStatusReason" in data:
        out["received_status_reason"] = data["ReceivedStatusReason"]
    if "AllowedOperations" in data:
        import aws_sdk_license_manager.types.allowed_operation_list

        out["allowed_operations"] = (
            aws_sdk_license_manager.types.allowed_operation_list.deserialize_aws_json_1_1(
                data["AllowedOperations"]
            )
        )
    return out
