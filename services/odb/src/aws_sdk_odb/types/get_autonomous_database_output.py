"""Generated from Smithy shape ``com.amazonaws.odb#GetAutonomousDatabaseOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.autonomous_database


class GetAutonomousDatabaseOutput(TypedDict, closed=True):
    autonomous_database: "aws_sdk_odb.types.autonomous_database.AutonomousDatabase"
    """<p>The details of the requested Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAutonomousDatabaseOutput) -> dict:
    out: dict = {}
    import aws_sdk_odb.types.autonomous_database

    out["autonomousDatabase"] = (
        aws_sdk_odb.types.autonomous_database.serialize_aws_json_1_0(
            value["autonomous_database"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAutonomousDatabaseOutput:
    out: GetAutonomousDatabaseOutput = {}  # type: ignore[typeddict-item]
    if "autonomousDatabase" in data:
        import aws_sdk_odb.types.autonomous_database

        out["autonomous_database"] = (
            aws_sdk_odb.types.autonomous_database.deserialize_aws_json_1_0(
                data["autonomousDatabase"]
            )
        )
    else:
        raise DeserializationError(
            "GetAutonomousDatabaseOutput.autonomous_database required"
        )
    return out
