"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RecommendedActionFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.filter_values
    import aws_sdk_compute_optimizer_automation.types.recommended_action_filter_name


class RecommendedActionFilter(TypedDict):
    name: "aws_sdk_compute_optimizer_automation.types.recommended_action_filter_name.RecommendedActionFilterName"
    """<p>The name of the filter field to apply.</p>"""
    values: "aws_sdk_compute_optimizer_automation.types.filter_values.FilterValues"
    """<p>List of filter values to match against the specified filter name. Used to narrow down recommended actions based on specific criteria.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedActionFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_compute_optimizer_automation.types.filter_values

    out["values"] = (
        aws_sdk_compute_optimizer_automation.types.filter_values.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendedActionFilter:
    out: RecommendedActionFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RecommendedActionFilter.name required")
    if "values" in data:
        import aws_sdk_compute_optimizer_automation.types.filter_values

        out["values"] = (
            aws_sdk_compute_optimizer_automation.types.filter_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    else:
        raise DeserializationError("RecommendedActionFilter.values required")
    return out
