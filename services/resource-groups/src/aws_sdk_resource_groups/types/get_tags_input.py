"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GetTagsInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_arn_v2


class GetTagsInput(TypedDict):
    arn: "aws_sdk_resource_groups.types.group_arn_v2.GroupArnV2"
    """<p>The Amazon resource name (ARN) of the resource group whose tags you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTagsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTagsInput:
    out: GetTagsInput = {}  # type: ignore[typeddict-item]
    return out
