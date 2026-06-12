"""Generated from Smithy shape ``com.amazonaws.macie2#GetFindingsFilterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__integer
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.finding_criteria
    import aws_sdk_macie2.types.findings_filter_action
    import aws_sdk_macie2.types.tag_map


class GetFindingsFilterResponse(TypedDict):
    action: NotRequired[
        "aws_sdk_macie2.types.findings_filter_action.FindingsFilterAction"
    ]
    """<p>The action that's performed on findings that match the filter criteria (findingCriteria). Possible values are: ARCHIVE, suppress (automatically archive) the findings; and, NOOP, don't perform any action on the findings.</p>"""
    arn: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the filter.</p>"""
    description: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The custom description of the filter.</p>"""
    finding_criteria: NotRequired[
        "aws_sdk_macie2.types.finding_criteria.FindingCriteria"
    ]
    """<p>The criteria that's used to filter findings.</p>"""
    id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the filter.</p>"""
    name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The custom name of the filter.</p>"""
    position: NotRequired["aws_sdk_macie2.types.__integer.__integer"]
    """<p>The position of the filter in the list of saved filters on the Amazon Macie console. This value also determines the order in which the filter is applied to findings, relative to other filters that are also applied to the findings.</p>"""
    tags: NotRequired["aws_sdk_macie2.types.tag_map.TagMap"]
    """<p>A map of key-value pairs that specifies which tags (keys and values) are associated with the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsFilterResponse) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_macie2.types.findings_filter_action

        out["action"] = aws_sdk_macie2.types.findings_filter_action.serialize_json(
            value["action"]
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "finding_criteria" in value:
        import aws_sdk_macie2.types.finding_criteria

        out["findingCriteria"] = aws_sdk_macie2.types.finding_criteria.serialize_json(
            value["finding_criteria"]
        )
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "position" in value:
        out["position"] = value["position"]
    if "tags" in value:
        import aws_sdk_macie2.types.tag_map

        out["tags"] = aws_sdk_macie2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetFindingsFilterResponse:
    out: GetFindingsFilterResponse = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_macie2.types.findings_filter_action

        out["action"] = aws_sdk_macie2.types.findings_filter_action.deserialize_json(
            data["action"]
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "description" in data:
        out["description"] = data["description"]
    if "findingCriteria" in data:
        import aws_sdk_macie2.types.finding_criteria

        out["finding_criteria"] = (
            aws_sdk_macie2.types.finding_criteria.deserialize_json(
                data["findingCriteria"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "position" in data:
        out["position"] = data["position"]
    if "tags" in data:
        import aws_sdk_macie2.types.tag_map

        out["tags"] = aws_sdk_macie2.types.tag_map.deserialize_json(data["tags"])
    return out
