"""Generated from Smithy shape ``com.amazonaws.wafregional#TagInfoForResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.resource_arn
    import aws_sdk_waf_regional.types.tag_list


class TagInfoForResource(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_waf_regional.types.resource_arn.ResourceArn"]
    """<p></p>"""
    tag_list: NotRequired["aws_sdk_waf_regional.types.tag_list.TagList"]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagInfoForResource) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "tag_list" in value:
        import aws_sdk_waf_regional.types.tag_list

        out["TagList"] = aws_sdk_waf_regional.types.tag_list.serialize_aws_json_1_1(
            value["tag_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagInfoForResource:
    out: TagInfoForResource = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "TagList" in data:
        import aws_sdk_waf_regional.types.tag_list

        out["tag_list"] = aws_sdk_waf_regional.types.tag_list.deserialize_aws_json_1_1(
            data["TagList"]
        )
    return out
