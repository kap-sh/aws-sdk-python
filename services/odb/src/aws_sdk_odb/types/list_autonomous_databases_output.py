"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousDatabasesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.autonomous_database_list


class ListAutonomousDatabasesOutput(TypedDict):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    autonomous_databases: (
        "aws_sdk_odb.types.autonomous_database_list.AutonomousDatabaseList"
    )
    """<p>The list of Autonomous Databases along with their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousDatabasesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_odb.types.autonomous_database_list

    out["autonomousDatabases"] = (
        aws_sdk_odb.types.autonomous_database_list.serialize_aws_json_1_0(
            value["autonomous_databases"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousDatabasesOutput:
    out: ListAutonomousDatabasesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "autonomousDatabases" in data:
        import aws_sdk_odb.types.autonomous_database_list

        out["autonomous_databases"] = (
            aws_sdk_odb.types.autonomous_database_list.deserialize_aws_json_1_0(
                data["autonomousDatabases"]
            )
        )
    else:
        raise DeserializationError(
            "ListAutonomousDatabasesOutput.autonomous_databases required"
        )
    return out
