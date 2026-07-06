"""Generated from Smithy shape ``com.amazonaws.guardduty#GetFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.filter_action
    import aws_sdk_guardduty.types.filter_description
    import aws_sdk_guardduty.types.filter_name
    import aws_sdk_guardduty.types.filter_rank
    import aws_sdk_guardduty.types.finding_criteria
    import aws_sdk_guardduty.types.tag_map


class GetFilterResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_guardduty.types.filter_name.FilterName"]
    """<p>The name of the filter.</p>"""
    description: NotRequired[
        "aws_sdk_guardduty.types.filter_description.FilterDescription"
    ]
    """<p>The description of the filter.</p>"""
    action: NotRequired["aws_sdk_guardduty.types.filter_action.FilterAction"]
    """<p>Specifies the action that is to be applied to the findings that match the filter.</p>"""
    rank: NotRequired["aws_sdk_guardduty.types.filter_rank.FilterRank"]
    """<p>Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.</p>"""
    finding_criteria: NotRequired[
        "aws_sdk_guardduty.types.finding_criteria.FindingCriteria"
    ]
    """<p>Represents the criteria to be used in the filter for querying findings.</p>"""
    tags: NotRequired["aws_sdk_guardduty.types.tag_map.TagMap"]
    """<p>The tags of the filter resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFilterResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "action" in value:
        import aws_sdk_guardduty.types.filter_action

        out["action"] = aws_sdk_guardduty.types.filter_action.serialize_json(
            value["action"]
        )
    if "rank" in value:
        out["rank"] = value["rank"]
    if "finding_criteria" in value:
        import aws_sdk_guardduty.types.finding_criteria

        out["findingCriteria"] = (
            aws_sdk_guardduty.types.finding_criteria.serialize_json(
                value["finding_criteria"]
            )
        )
    if "tags" in value:
        import aws_sdk_guardduty.types.tag_map

        out["tags"] = aws_sdk_guardduty.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetFilterResponse:
    out: GetFilterResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "action" in data:
        import aws_sdk_guardduty.types.filter_action

        out["action"] = aws_sdk_guardduty.types.filter_action.deserialize_json(
            data["action"]
        )
    if "rank" in data:
        out["rank"] = data["rank"]
    if "findingCriteria" in data:
        import aws_sdk_guardduty.types.finding_criteria

        out["finding_criteria"] = (
            aws_sdk_guardduty.types.finding_criteria.deserialize_json(
                data["findingCriteria"]
            )
        )
    if "tags" in data:
        import aws_sdk_guardduty.types.tag_map

        out["tags"] = aws_sdk_guardduty.types.tag_map.deserialize_json(data["tags"])
    return out
