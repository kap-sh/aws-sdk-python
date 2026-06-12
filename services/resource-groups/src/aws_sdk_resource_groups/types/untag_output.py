"""Generated from Smithy shape ``com.amazonaws.resourcegroups#UntagOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_arn_v2
    import aws_sdk_resource_groups.types.tag_key_list


class UntagOutput(TypedDict):
    arn: NotRequired["aws_sdk_resource_groups.types.group_arn_v2.GroupArnV2"]
    """<p>The Amazon resource name (ARN) of the resource group from which tags have been removed.</p>"""
    keys: NotRequired["aws_sdk_resource_groups.types.tag_key_list.TagKeyList"]
    """<p>The keys of the tags that were removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "keys" in value:
        import aws_sdk_resource_groups.types.tag_key_list

        out["Keys"] = aws_sdk_resource_groups.types.tag_key_list.serialize_json(
            value["keys"]
        )
    return out


def deserialize_json(data: dict) -> UntagOutput:
    out: UntagOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Keys" in data:
        import aws_sdk_resource_groups.types.tag_key_list

        out["keys"] = aws_sdk_resource_groups.types.tag_key_list.deserialize_json(
            data["Keys"]
        )
    return out
