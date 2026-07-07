"""Generated from Smithy shape ``com.amazonaws.codepipeline#TargetFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.target_filter_name
    import aws_sdk_codepipeline.types.target_filter_value_list


class TargetFilter(TypedDict, closed=True):
    name: NotRequired["aws_sdk_codepipeline.types.target_filter_name.TargetFilterName"]
    """<p>The name on which to filter.</p>"""
    values: NotRequired[
        "aws_sdk_codepipeline.types.target_filter_value_list.TargetFilterValueList"
    ]
    """<p>The values on which to filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_codepipeline.types.target_filter_name

        out["name"] = (
            aws_sdk_codepipeline.types.target_filter_name.serialize_aws_json_1_1(
                value["name"]
            )
        )
    if "values" in value:
        import aws_sdk_codepipeline.types.target_filter_value_list

        out["values"] = (
            aws_sdk_codepipeline.types.target_filter_value_list.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetFilter:
    out: TargetFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_codepipeline.types.target_filter_name

        out["name"] = (
            aws_sdk_codepipeline.types.target_filter_name.deserialize_aws_json_1_1(
                data["name"]
            )
        )
    if "values" in data:
        import aws_sdk_codepipeline.types.target_filter_value_list

        out["values"] = (
            aws_sdk_codepipeline.types.target_filter_value_list.deserialize_aws_json_1_1(
                data["values"]
            )
        )
    return out
