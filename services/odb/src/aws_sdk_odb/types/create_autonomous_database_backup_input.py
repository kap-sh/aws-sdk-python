"""Generated from Smithy shape ``com.amazonaws.odb#CreateAutonomousDatabaseBackupInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.general_input_string
    import aws_sdk_odb.types.request_tag_map
    import aws_sdk_odb.types.resource_display_name
    import aws_sdk_odb.types.resource_id_or_arn


class CreateAutonomousDatabaseBackupInput(TypedDict):
    autonomous_database_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database to back up.</p>"""
    display_name: NotRequired[
        "aws_sdk_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>The user-friendly name for the Autonomous Database backup.</p>"""
    retention_period_in_days: NotRequired["int"]
    """<p>The retention period, in days, for the Autonomous Database backup.</p>"""
    client_token: NotRequired[
        "aws_sdk_odb.types.general_input_string.GeneralInputString"
    ]
    """<p>A client-provided token to ensure the idempotency of the request.</p>"""
    tags: NotRequired["aws_sdk_odb.types.request_tag_map.RequestTagMap"]
    """<p>The list of resource tags to apply to the Autonomous Database backup. Each tag is a key-value pair with no predefined name, type, or namespace.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAutonomousDatabaseBackupInput) -> dict:
    out: dict = {}
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "retention_period_in_days" in value:
        out["retentionPeriodInDays"] = value["retention_period_in_days"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_odb.types.request_tag_map

        out["tags"] = aws_sdk_odb.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAutonomousDatabaseBackupInput:
    out: CreateAutonomousDatabaseBackupInput = {}  # type: ignore[typeddict-item]
    if "autonomousDatabaseId" in data:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        raise DeserializationError(
            "CreateAutonomousDatabaseBackupInput.autonomous_database_id required"
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "retentionPeriodInDays" in data:
        out["retention_period_in_days"] = data["retentionPeriodInDays"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_odb.types.request_tag_map

        out["tags"] = aws_sdk_odb.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
