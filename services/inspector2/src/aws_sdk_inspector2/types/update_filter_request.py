"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.filter_action
    import aws_sdk_inspector2.types.filter_arn
    import aws_sdk_inspector2.types.filter_criteria
    import aws_sdk_inspector2.types.filter_description
    import aws_sdk_inspector2.types.filter_name
    import aws_sdk_inspector2.types.filter_reason


class UpdateFilterRequest(TypedDict, closed=True):
    action: NotRequired["aws_sdk_inspector2.types.filter_action.FilterAction"]
    """<p>Specifies the action that is to be applied to the findings that match the filter.</p>"""
    description: NotRequired[
        "aws_sdk_inspector2.types.filter_description.FilterDescription"
    ]
    """<p>A description of the filter.</p>"""
    filter_criteria: NotRequired[
        "aws_sdk_inspector2.types.filter_criteria.FilterCriteria"
    ]
    """<p>Defines the criteria to be update in the filter.</p>"""
    name: NotRequired["aws_sdk_inspector2.types.filter_name.FilterName"]
    """<p>The name of the filter.</p>"""
    filter_arn: "aws_sdk_inspector2.types.filter_arn.FilterArn"
    """<p>The Amazon Resource Number (ARN) of the filter to update.</p>"""
    reason: NotRequired["aws_sdk_inspector2.types.filter_reason.FilterReason"]
    """<p>The reason the filter was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFilterRequest) -> dict:
    out: dict = {}
    if "action" in value:
        out["action"] = value["action"]
    if "description" in value:
        out["description"] = value["description"]
    if "filter_criteria" in value:
        import aws_sdk_inspector2.types.filter_criteria

        out["filterCriteria"] = aws_sdk_inspector2.types.filter_criteria.serialize_json(
            value["filter_criteria"]
        )
    if "name" in value:
        out["name"] = value["name"]
    out["filterArn"] = value["filter_arn"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> UpdateFilterRequest:
    out: UpdateFilterRequest = {}  # type: ignore[typeddict-item]
    if "action" in data:
        out["action"] = data["action"]
    if "description" in data:
        out["description"] = data["description"]
    if "filterCriteria" in data:
        import aws_sdk_inspector2.types.filter_criteria

        out["filter_criteria"] = (
            aws_sdk_inspector2.types.filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "filterArn" in data:
        out["filter_arn"] = data["filterArn"]
    else:
        raise DeserializationError("UpdateFilterRequest.filter_arn required")
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
