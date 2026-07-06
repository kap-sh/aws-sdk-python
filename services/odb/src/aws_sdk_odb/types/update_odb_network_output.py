"""Generated from Smithy shape ``com.amazonaws.odb#UpdateOdbNetworkOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_status


class UpdateOdbNetworkOutput(TypedDict, closed=True):
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the ODB network.</p>"""
    status: NotRequired["aws_sdk_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the ODB network.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the ODB network.</p>"""
    odb_network_id: "str"
    """<p>The unique identifier of the ODB network.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateOdbNetworkOutput) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import aws_sdk_odb.types.resource_status

        out["status"] = aws_sdk_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    out["odbNetworkId"] = value["odb_network_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateOdbNetworkOutput:
    out: UpdateOdbNetworkOutput = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "status" in data:
        import aws_sdk_odb.types.resource_status

        out["status"] = aws_sdk_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "odbNetworkId" in data:
        out["odb_network_id"] = data["odbNetworkId"]
    else:
        raise DeserializationError("UpdateOdbNetworkOutput.odb_network_id required")
    return out
