"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ApplicationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auto_scaling_plans.types.tag_filters
    import aws_sdk_auto_scaling_plans.types.xml_string


class ApplicationSource(TypedDict, closed=True):
    cloud_formation_stack_arn: NotRequired[
        "aws_sdk_auto_scaling_plans.types.xml_string.XmlString"
    ]
    """<p>The Amazon Resource Name (ARN) of a AWS CloudFormation stack.</p>"""
    tag_filters: NotRequired["aws_sdk_auto_scaling_plans.types.tag_filters.TagFilters"]
    """<p>A set of tags (up to 50).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSource) -> dict:
    out: dict = {}
    if "cloud_formation_stack_arn" in value:
        out["CloudFormationStackARN"] = value["cloud_formation_stack_arn"]
    if "tag_filters" in value:
        import aws_sdk_auto_scaling_plans.types.tag_filters

        out["TagFilters"] = (
            aws_sdk_auto_scaling_plans.types.tag_filters.serialize_aws_json_1_1(
                value["tag_filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSource:
    out: ApplicationSource = {}  # type: ignore[typeddict-item]
    if "CloudFormationStackARN" in data:
        out["cloud_formation_stack_arn"] = data["CloudFormationStackARN"]
    if "TagFilters" in data:
        import aws_sdk_auto_scaling_plans.types.tag_filters

        out["tag_filters"] = (
            aws_sdk_auto_scaling_plans.types.tag_filters.deserialize_aws_json_1_1(
                data["TagFilters"]
            )
        )
    return out
