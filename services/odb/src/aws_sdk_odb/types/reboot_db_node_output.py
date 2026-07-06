"""Generated from Smithy shape ``com.amazonaws.odb#RebootDbNodeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.db_node_resource_status


class RebootDbNodeOutput(TypedDict, closed=True):
    db_node_id: "str"
    """<p>The unique identifier of the DB node that was rebooted.</p>"""
    status: NotRequired[
        "aws_sdk_odb.types.db_node_resource_status.DbNodeResourceStatus"
    ]
    """<p>The current status of the DB node after the reboot operation.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the DB node after the reboot operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RebootDbNodeOutput) -> dict:
    out: dict = {}
    out["dbNodeId"] = value["db_node_id"]
    if "status" in value:
        import aws_sdk_odb.types.db_node_resource_status

        out["status"] = (
            aws_sdk_odb.types.db_node_resource_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RebootDbNodeOutput:
    out: RebootDbNodeOutput = {}  # type: ignore[typeddict-item]
    if "dbNodeId" in data:
        out["db_node_id"] = data["dbNodeId"]
    else:
        raise DeserializationError("RebootDbNodeOutput.db_node_id required")
    if "status" in data:
        import aws_sdk_odb.types.db_node_resource_status

        out["status"] = (
            aws_sdk_odb.types.db_node_resource_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
