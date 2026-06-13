"""Generated from Smithy shape ``com.amazonaws.odb#StopAutonomousDatabaseInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id_or_arn


class StopAutonomousDatabaseInput(TypedDict):
    autonomous_database_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database to stop.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopAutonomousDatabaseInput) -> dict:
    out: dict = {}
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StopAutonomousDatabaseInput:
    out: StopAutonomousDatabaseInput = {}  # type: ignore[typeddict-item]
    if "autonomousDatabaseId" in data:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        raise DeserializationError(
            "StopAutonomousDatabaseInput.autonomous_database_id required"
        )
    return out
