"""Generated from Smithy shape ``com.amazonaws.odb#RestoreAutonomousDatabaseInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_odb.types.resource_id_or_arn


class RestoreAutonomousDatabaseInput(TypedDict):
    autonomous_database_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Autonomous Database to restore.</p>"""
    timestamp: "datetime.datetime"
    """<p>The date and time to which to restore the Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreAutonomousDatabaseInput) -> dict:
    out: dict = {}
    out["autonomousDatabaseId"] = value["autonomous_database_id"]
    import aws_sdk_odb.types._prelude.timestamp

    out["timestamp"] = aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
        value["timestamp"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreAutonomousDatabaseInput:
    out: RestoreAutonomousDatabaseInput = {}  # type: ignore[typeddict-item]
    if "autonomousDatabaseId" in data:
        out["autonomous_database_id"] = data["autonomousDatabaseId"]
    else:
        raise DeserializationError(
            "RestoreAutonomousDatabaseInput.autonomous_database_id required"
        )
    if "timestamp" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("RestoreAutonomousDatabaseInput.timestamp required")
    return out
