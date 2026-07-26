"""Generated from Smithy shape ``com.amazonaws.wafv2#TagInfoForResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.resource_arn
    import capo_wafv2.types.tag_list


class TagInfoForResource(TypedDict, closed=True):
    resource_arn: NotRequired["capo_wafv2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_list: NotRequired["capo_wafv2.types.tag_list.TagList"]
    """<p>The array of <a>Tag</a> objects defined for the resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagInfoForResource) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "tag_list" in value:
        import capo_wafv2.types.tag_list

        out["TagList"] = capo_wafv2.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagInfoForResource:
    out: TagInfoForResource = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "TagList" in data:
        import capo_wafv2.types.tag_list

        out["tag_list"] = capo_wafv2.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out
