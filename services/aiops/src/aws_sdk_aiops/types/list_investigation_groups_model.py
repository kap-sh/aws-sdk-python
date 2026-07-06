"""Generated from Smithy shape ``com.amazonaws.aiops#ListInvestigationGroupsModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_aiops.types.investigation_group_arn
    import aws_sdk_aiops.types.string_with_pattern_and_length_limits


class ListInvestigationGroupsModel(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_aiops.types.investigation_group_arn.InvestigationGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the investigation group.</p>"""
    name: NotRequired[
        "aws_sdk_aiops.types.string_with_pattern_and_length_limits.StringWithPatternAndLengthLimits"
    ]
    """<p>The name of the investigation group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvestigationGroupsModel) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ListInvestigationGroupsModel:
    out: ListInvestigationGroupsModel = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    return out
