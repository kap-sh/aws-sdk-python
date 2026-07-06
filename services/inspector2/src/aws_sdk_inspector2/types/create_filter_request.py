"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.filter_action
    import aws_sdk_inspector2.types.filter_criteria
    import aws_sdk_inspector2.types.filter_description
    import aws_sdk_inspector2.types.filter_name
    import aws_sdk_inspector2.types.filter_reason
    import aws_sdk_inspector2.types.tag_map


class CreateFilterRequest(TypedDict, closed=True):
    action: "aws_sdk_inspector2.types.filter_action.FilterAction"
    """<p>Defines the action that is to be applied to the findings that match the filter.</p>"""
    description: NotRequired[
        "aws_sdk_inspector2.types.filter_description.FilterDescription"
    ]
    """<p>A description of the filter.</p>"""
    filter_criteria: "aws_sdk_inspector2.types.filter_criteria.FilterCriteria"
    """<p>Defines the criteria to be used in the filter for querying findings.</p>"""
    name: "aws_sdk_inspector2.types.filter_name.FilterName"
    """<p>The name of the filter. Minimum length of 3. Maximum length of 64. Valid characters include alphanumeric characters, dot (.), underscore (_), and dash (-). Spaces are not allowed.</p>"""
    tags: NotRequired["aws_sdk_inspector2.types.tag_map.TagMap"]
    """<p>A list of tags for the filter.</p>"""
    reason: NotRequired["aws_sdk_inspector2.types.filter_reason.FilterReason"]
    """<p>The reason for creating the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFilterRequest) -> dict:
    out: dict = {}
    out["action"] = value["action"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_inspector2.types.filter_criteria

    out["filterCriteria"] = aws_sdk_inspector2.types.filter_criteria.serialize_json(
        value["filter_criteria"]
    )
    out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.serialize_json(value["tags"])
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> CreateFilterRequest:
    out: CreateFilterRequest = {}  # type: ignore[typeddict-item]
    if "action" in data:
        out["action"] = data["action"]
    else:
        raise DeserializationError("CreateFilterRequest.action required")
    if "description" in data:
        out["description"] = data["description"]
    if "filterCriteria" in data:
        import aws_sdk_inspector2.types.filter_criteria

        out["filter_criteria"] = (
            aws_sdk_inspector2.types.filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    else:
        raise DeserializationError("CreateFilterRequest.filter_criteria required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateFilterRequest.name required")
    if "tags" in data:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.deserialize_json(data["tags"])
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
