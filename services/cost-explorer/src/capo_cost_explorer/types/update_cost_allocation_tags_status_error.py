"""Generated from Smithy shape ``com.amazonaws.costexplorer#UpdateCostAllocationTagsStatusError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.error_message
    import capo_cost_explorer.types.generic_string
    import capo_cost_explorer.types.tag_key


class UpdateCostAllocationTagsStatusError(TypedDict, closed=True):
    tag_key: NotRequired["capo_cost_explorer.types.tag_key.TagKey"]
    """<p>The key for the cost allocation tag. </p>"""
    code: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>An error code representing why the action failed on this entry. </p>"""
    message: NotRequired["capo_cost_explorer.types.error_message.ErrorMessage"]
    """<p>A message explaining why the action failed on this entry. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCostAllocationTagsStatusError) -> dict:
    out: dict = {}
    if "tag_key" in value:
        out["TagKey"] = value["tag_key"]
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCostAllocationTagsStatusError:
    out: UpdateCostAllocationTagsStatusError = {}  # type: ignore[typeddict-item]
    if "TagKey" in data:
        out["tag_key"] = data["TagKey"]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
