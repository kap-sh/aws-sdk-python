"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabasePeerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_arn
    import aws_sdk_odb.types.resource_id


class AutonomousDatabasePeerSummary(TypedDict, closed=True):
    autonomous_database_id: NotRequired["aws_sdk_odb.types.resource_id.ResourceId"]
    """<p>The unique identifier of the peer Autonomous Database.</p>"""
    autonomous_database_arn: NotRequired["aws_sdk_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the peer Autonomous Database.</p>"""
    ocid: NotRequired["str"]
    """<p>The Oracle Cloud Identifier (OCID) of the peer Autonomous Database.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region where the peer Autonomous Database is located.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabasePeerSummary) -> dict:
    out: dict = {}
    if "autonomous_database_id" in value:
        out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "autonomous_database_arn" in value:
        out["autonomousDatabaseArn"] = value["autonomous_database_arn"]
    if "ocid" in value:
        out["ocid"] = value["ocid"]
    if "region" in value:
        out["region"] = value["region"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AutonomousDatabasePeerSummary:
    out: AutonomousDatabasePeerSummary = {}  # type: ignore[typeddict-item]
    if "autonomousDatabaseId" in data:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    if "autonomousDatabaseArn" in data:
        out["autonomous_database_arn"] = data["autonomousDatabaseArn"]
    if "ocid" in data:
        out["ocid"] = data["ocid"]
    if "region" in data:
        out["region"] = data["region"]
    return out
