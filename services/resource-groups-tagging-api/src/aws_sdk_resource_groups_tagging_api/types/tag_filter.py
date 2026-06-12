"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#TagFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.tag_key
    import aws_sdk_resource_groups_tagging_api.types.tag_value_list


class TagFilter(TypedDict):
    key: NotRequired["aws_sdk_resource_groups_tagging_api.types.tag_key.TagKey"]
    """<p>One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.</p>"""
    values: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.tag_value_list.TagValueList"
    ]
    """<p>One part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import aws_sdk_resource_groups_tagging_api.types.tag_value_list

        out["Values"] = (
            aws_sdk_resource_groups_tagging_api.types.tag_value_list.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Values" in data:
        import aws_sdk_resource_groups_tagging_api.types.tag_value_list

        out["values"] = (
            aws_sdk_resource_groups_tagging_api.types.tag_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
