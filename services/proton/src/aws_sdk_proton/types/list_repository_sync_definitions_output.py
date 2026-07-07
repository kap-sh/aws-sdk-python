"""Generated from Smithy shape ``com.amazonaws.proton#ListRepositorySyncDefinitionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.empty_next_token
    import aws_sdk_proton.types.repository_sync_definition_list


class ListRepositorySyncDefinitionsOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_proton.types.empty_next_token.EmptyNextToken"]
    """<p>A token that indicates the location of the next repository sync definition in the array of repository sync definitions, after the current requested list of repository sync definitions.</p>"""
    sync_definitions: "aws_sdk_proton.types.repository_sync_definition_list.RepositorySyncDefinitionList"
    """<p>An array of repository sync definitions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRepositorySyncDefinitionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_proton.types.repository_sync_definition_list

    out["syncDefinitions"] = (
        aws_sdk_proton.types.repository_sync_definition_list.serialize_aws_json_1_0(
            value["sync_definitions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRepositorySyncDefinitionsOutput:
    out: ListRepositorySyncDefinitionsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "syncDefinitions" in data:
        import aws_sdk_proton.types.repository_sync_definition_list

        out["sync_definitions"] = (
            aws_sdk_proton.types.repository_sync_definition_list.deserialize_aws_json_1_0(
                data["syncDefinitions"]
            )
        )
    else:
        raise DeserializationError(
            "ListRepositorySyncDefinitionsOutput.sync_definitions required"
        )
    return out
