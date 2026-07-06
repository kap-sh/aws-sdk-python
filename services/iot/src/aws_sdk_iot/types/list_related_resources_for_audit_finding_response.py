"""Generated from Smithy shape ``com.amazonaws.iot#ListRelatedResourcesForAuditFindingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.related_resources


class ListRelatedResourcesForAuditFindingResponse(TypedDict, closed=True):
    related_resources: NotRequired[
        "aws_sdk_iot.types.related_resources.RelatedResources"
    ]
    """<p>The related resources.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or <code>null</code> for the first API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRelatedResourcesForAuditFindingResponse) -> dict:
    out: dict = {}
    if "related_resources" in value:
        import aws_sdk_iot.types.related_resources

        out["relatedResources"] = aws_sdk_iot.types.related_resources.serialize_json(
            value["related_resources"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRelatedResourcesForAuditFindingResponse:
    out: ListRelatedResourcesForAuditFindingResponse = {}  # type: ignore[typeddict-item]
    if "relatedResources" in data:
        import aws_sdk_iot.types.related_resources

        out["related_resources"] = aws_sdk_iot.types.related_resources.deserialize_json(
            data["relatedResources"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
