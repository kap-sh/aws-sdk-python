"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousDatabaseClonesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.autonomous_database_list


class ListAutonomousDatabaseClonesOutput(TypedDict):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    autonomous_database_clones: (
        "aws_sdk_odb.types.autonomous_database_list.AutonomousDatabaseList"
    )
    """<p>The list of Autonomous Database clones along with their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousDatabaseClonesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_odb.types.autonomous_database_list

    out["autonomousDatabaseClones"] = (
        aws_sdk_odb.types.autonomous_database_list.serialize_aws_json_1_0(
            value["autonomous_database_clones"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousDatabaseClonesOutput:
    out: ListAutonomousDatabaseClonesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "autonomousDatabaseClones" in data:
        import aws_sdk_odb.types.autonomous_database_list

        out["autonomous_database_clones"] = (
            aws_sdk_odb.types.autonomous_database_list.deserialize_aws_json_1_0(
                data["autonomousDatabaseClones"]
            )
        )
    else:
        raise DeserializationError(
            "ListAutonomousDatabaseClonesOutput.autonomous_database_clones required"
        )
    return out
