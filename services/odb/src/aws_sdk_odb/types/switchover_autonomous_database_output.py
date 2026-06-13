"""Generated from Smithy shape ``com.amazonaws.odb#SwitchoverAutonomousDatabaseOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.autonomous_database_resource_status


class SwitchoverAutonomousDatabaseOutput(TypedDict):
    autonomous_database_id: "str"
    """<p>The unique identifier of the Autonomous Database that was switched over.</p>"""
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the Autonomous Database.</p>"""
    status: NotRequired[
        "aws_sdk_odb.types.autonomous_database_resource_status.AutonomousDatabaseResourceStatus"
    ]
    """<p>The current status of the Autonomous Database after the switchover operation.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the status of the Autonomous Database after the switchover operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SwitchoverAutonomousDatabaseOutput) -> dict:
    out: dict = {}
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import aws_sdk_odb.types.autonomous_database_resource_status

        out["status"] = (
            aws_sdk_odb.types.autonomous_database_resource_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SwitchoverAutonomousDatabaseOutput:
    out: SwitchoverAutonomousDatabaseOutput = {}  # type: ignore[typeddict-item]
    if "autonomousDatabaseId" in data:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        raise DeserializationError(
            "SwitchoverAutonomousDatabaseOutput.autonomous_database_id required"
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "status" in data:
        import aws_sdk_odb.types.autonomous_database_resource_status

        out["status"] = (
            aws_sdk_odb.types.autonomous_database_resource_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
