"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#TagFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.tag_values
    import aws_sdk_auto_scaling_plans.types.xml_string_max_len128


class TagFilter(TypedDict):
    key: NotRequired[
        "aws_sdk_auto_scaling_plans.types.xml_string_max_len128.XmlStringMaxLen128"
    ]
    """<p>The tag key.</p>"""
    values: NotRequired["aws_sdk_auto_scaling_plans.types.tag_values.TagValues"]
    """<p>The tag values (0 to 20).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import aws_sdk_auto_scaling_plans.types.tag_values

        out["Values"] = (
            aws_sdk_auto_scaling_plans.types.tag_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Values" in data:
        import aws_sdk_auto_scaling_plans.types.tag_values

        out["values"] = (
            aws_sdk_auto_scaling_plans.types.tag_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
