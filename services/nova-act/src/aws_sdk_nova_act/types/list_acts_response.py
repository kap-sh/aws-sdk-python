"""Generated from Smithy shape ``com.amazonaws.novaact#ListActsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.act_summaries
    import aws_sdk_nova_act.types.next_token


class ListActsResponse(TypedDict):
    act_summaries: "aws_sdk_nova_act.types.act_summaries.ActSummaries"
    """<p>A list of summary information for acts in the session.</p>"""
    next_token: NotRequired["aws_sdk_nova_act.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results, if available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActsResponse) -> dict:
    out: dict = {}
    import aws_sdk_nova_act.types.act_summaries

    out["actSummaries"] = aws_sdk_nova_act.types.act_summaries.serialize_json(
        value["act_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListActsResponse:
    out: ListActsResponse = {}  # type: ignore[typeddict-item]
    if "actSummaries" in data:
        import aws_sdk_nova_act.types.act_summaries

        out["act_summaries"] = aws_sdk_nova_act.types.act_summaries.deserialize_json(
            data["actSummaries"]
        )
    else:
        raise DeserializationError("ListActsResponse.act_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
