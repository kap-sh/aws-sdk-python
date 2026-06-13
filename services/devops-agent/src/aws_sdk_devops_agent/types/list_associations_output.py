"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListAssociationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.associations_list
    import aws_sdk_devops_agent.types.next_token


class ListAssociationsOutput(TypedDict):
    next_token: NotRequired["aws_sdk_devops_agent.types.next_token.NextToken"]
    """<p>Token to retrieve the next page of results, if there are more results.</p>"""
    associations: "aws_sdk_devops_agent.types.associations_list.AssociationsList"
    """<p>The list of associations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociationsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_devops_agent.types.associations_list

    out["associations"] = aws_sdk_devops_agent.types.associations_list.serialize_json(
        value["associations"]
    )
    return out


def deserialize_json(data: dict) -> ListAssociationsOutput:
    out: ListAssociationsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "associations" in data:
        import aws_sdk_devops_agent.types.associations_list

        out["associations"] = (
            aws_sdk_devops_agent.types.associations_list.deserialize_json(
                data["associations"]
            )
        )
    else:
        raise DeserializationError("ListAssociationsOutput.associations required")
    return out
