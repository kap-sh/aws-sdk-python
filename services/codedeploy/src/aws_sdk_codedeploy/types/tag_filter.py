"""Generated from Smithy shape ``com.amazonaws.codedeploy#TagFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.key
    import aws_sdk_codedeploy.types.tag_filter_type
    import aws_sdk_codedeploy.types.value


class TagFilter(TypedDict):
    key: NotRequired["aws_sdk_codedeploy.types.key.Key"]
    """<p>The on-premises instance tag filter key.</p>"""
    value: NotRequired["aws_sdk_codedeploy.types.value.Value"]
    """<p>The on-premises instance tag filter value.</p>"""
    type: NotRequired["aws_sdk_codedeploy.types.tag_filter_type.TagFilterType"]
    """<p>The on-premises instance tag filter type:</p> <ul> <li> <p>KEY_ONLY: Key only.</p> </li> <li> <p>VALUE_ONLY: Value only.</p> </li> <li> <p>KEY_AND_VALUE: Key and value.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    if "type" in value:
        import aws_sdk_codedeploy.types.tag_filter_type

        out["Type"] = aws_sdk_codedeploy.types.tag_filter_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Type" in data:
        import aws_sdk_codedeploy.types.tag_filter_type

        out["type"] = aws_sdk_codedeploy.types.tag_filter_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
