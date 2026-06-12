"""Generated from Smithy shape ``com.amazonaws.connect#FilterV2StringCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.filter_v2_string_condition_comparison_operator


class FilterV2StringCondition(TypedDict):
    comparison: NotRequired[
        "aws_sdk_connect.types.filter_v2_string_condition_comparison_operator.FilterV2StringConditionComparisonOperator"
    ]
    """<p> The string condition. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterV2StringCondition) -> dict:
    out: dict = {}
    if "comparison" in value:
        import aws_sdk_connect.types.filter_v2_string_condition_comparison_operator

        out["Comparison"] = (
            aws_sdk_connect.types.filter_v2_string_condition_comparison_operator.serialize_json(
                value["comparison"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterV2StringCondition:
    out: FilterV2StringCondition = {}  # type: ignore[typeddict-item]
    if "Comparison" in data:
        import aws_sdk_connect.types.filter_v2_string_condition_comparison_operator

        out["comparison"] = (
            aws_sdk_connect.types.filter_v2_string_condition_comparison_operator.deserialize_json(
                data["Comparison"]
            )
        )
    return out
