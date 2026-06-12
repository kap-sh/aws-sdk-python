"""Generated from Smithy shape ``com.amazonaws.guardduty#ListFindingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.finding_ids
    import aws_sdk_guardduty.types.string


class ListFindingsResponse(TypedDict):
    finding_ids: NotRequired["aws_sdk_guardduty.types.finding_ids.FindingIds"]
    """<p>The IDs of the findings that you're listing.</p>"""
    next_token: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsResponse) -> dict:
    out: dict = {}
    if "finding_ids" in value:
        import aws_sdk_guardduty.types.finding_ids

        out["findingIds"] = aws_sdk_guardduty.types.finding_ids.serialize_json(
            value["finding_ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFindingsResponse:
    out: ListFindingsResponse = {}  # type: ignore[typeddict-item]
    if "findingIds" in data:
        import aws_sdk_guardduty.types.finding_ids

        out["finding_ids"] = aws_sdk_guardduty.types.finding_ids.deserialize_json(
            data["findingIds"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
