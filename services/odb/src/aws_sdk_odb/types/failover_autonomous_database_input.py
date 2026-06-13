"""Generated from Smithy shape ``com.amazonaws.odb#FailoverAutonomousDatabaseInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_arn
    import aws_sdk_odb.types.resource_id_or_arn


class FailoverAutonomousDatabaseInput(TypedDict):
    autonomous_database_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database to fail over.</p>"""
    peer_db_arn: NotRequired["aws_sdk_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the peer Autonomous Database to fail over to.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FailoverAutonomousDatabaseInput) -> dict:
    out: dict = {}
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    if "peer_db_arn" in value:
        out["peerDbArn"] = value["peer_db_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FailoverAutonomousDatabaseInput:
    out: FailoverAutonomousDatabaseInput = {}  # type: ignore[typeddict-item]
    if "autonomousDatabaseId" in data:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        raise DeserializationError(
            "FailoverAutonomousDatabaseInput.autonomous_database_id required"
        )
    if "peerDbArn" in data:
        out["peer_db_arn"] = data["peerDbArn"]
    return out
