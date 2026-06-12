"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListPortalsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.next_token
    import aws_sdk_iotsitewise.types.portal_summaries


class ListPortalsResponse(TypedDict):
    portal_summaries: NotRequired[
        "aws_sdk_iotsitewise.types.portal_summaries.PortalSummaries"
    ]
    """<p>A list that summarizes each portal.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPortalsResponse) -> dict:
    out: dict = {}
    if "portal_summaries" in value:
        import aws_sdk_iotsitewise.types.portal_summaries

        out["portalSummaries"] = (
            aws_sdk_iotsitewise.types.portal_summaries.serialize_json(
                value["portal_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPortalsResponse:
    out: ListPortalsResponse = {}  # type: ignore[typeddict-item]
    if "portalSummaries" in data:
        import aws_sdk_iotsitewise.types.portal_summaries

        out["portal_summaries"] = (
            aws_sdk_iotsitewise.types.portal_summaries.deserialize_json(
                data["portalSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
