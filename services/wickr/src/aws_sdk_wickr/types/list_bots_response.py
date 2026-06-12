"""Generated from Smithy shape ``com.amazonaws.wickr#ListBotsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.bots
    import aws_sdk_wickr.types.generic_string


class ListBotsResponse(TypedDict):
    bots: "aws_sdk_wickr.types.bots.Bots"
    """<p>A list of bot objects matching the specified filters and within the current page.</p>"""
    next_token: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The token to use for retrieving the next page of results. If this is not present, there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotsResponse) -> dict:
    out: dict = {}
    import aws_sdk_wickr.types.bots

    out["bots"] = aws_sdk_wickr.types.bots.serialize_json(value["bots"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotsResponse:
    out: ListBotsResponse = {}  # type: ignore[typeddict-item]
    if "bots" in data:
        import aws_sdk_wickr.types.bots

        out["bots"] = aws_sdk_wickr.types.bots.deserialize_json(data["bots"])
    else:
        raise DeserializationError("ListBotsResponse.bots required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
