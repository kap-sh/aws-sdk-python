"""Generated from Smithy shape ``com.amazonaws.odb#StartAutonomousDatabaseInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id_or_arn


class StartAutonomousDatabaseInput(TypedDict, closed=True):
    autonomous_database_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database to start.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartAutonomousDatabaseInput) -> dict:
    out: dict = {}
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartAutonomousDatabaseInput:
    out: StartAutonomousDatabaseInput = {}  # type: ignore[typeddict-item]
    if "autonomousDatabaseId" in data:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        raise DeserializationError(
            "StartAutonomousDatabaseInput.autonomous_database_id required"
        )
    return out
