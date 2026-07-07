"""Generated from Smithy shape ``com.amazonaws.outposts#ListOutpostsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.outpost_list_definition
    import aws_sdk_outposts.types.token


class ListOutpostsOutput(TypedDict, closed=True):
    outposts: NotRequired[
        "aws_sdk_outposts.types.outpost_list_definition.outpostListDefinition"
    ]
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOutpostsOutput) -> dict:
    out: dict = {}
    if "outposts" in value:
        import aws_sdk_outposts.types.outpost_list_definition

        out["Outposts"] = aws_sdk_outposts.types.outpost_list_definition.serialize_json(
            value["outposts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOutpostsOutput:
    out: ListOutpostsOutput = {}  # type: ignore[typeddict-item]
    if "Outposts" in data:
        import aws_sdk_outposts.types.outpost_list_definition

        out["outposts"] = (
            aws_sdk_outposts.types.outpost_list_definition.deserialize_json(
                data["Outposts"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
