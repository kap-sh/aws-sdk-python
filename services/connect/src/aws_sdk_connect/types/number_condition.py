"""Generated from Smithy shape ``com.amazonaws.connect#NumberCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.nullable_proficiency_limit_value
    import aws_sdk_connect.types.number_comparison_type
    import aws_sdk_connect.types.string


class NumberCondition(TypedDict):
    field_name: NotRequired["aws_sdk_connect.types.string.String"]
    """<p>The name of the field in the number condition.</p>"""
    min_value: NotRequired[
        "aws_sdk_connect.types.nullable_proficiency_limit_value.NullableProficiencyLimitValue"
    ]
    """<p>The minValue to be used while evaluating the number condition.</p>"""
    max_value: NotRequired[
        "aws_sdk_connect.types.nullable_proficiency_limit_value.NullableProficiencyLimitValue"
    ]
    """<p>The maxValue to be used while evaluating the number condition.</p>"""
    comparison_type: NotRequired[
        "aws_sdk_connect.types.number_comparison_type.NumberComparisonType"
    ]
    """<p>The type of comparison to be made when evaluating the number condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumberCondition) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    if "min_value" in value:
        out["MinValue"] = value["min_value"]
    if "max_value" in value:
        out["MaxValue"] = value["max_value"]
    if "comparison_type" in value:
        import aws_sdk_connect.types.number_comparison_type

        out["ComparisonType"] = (
            aws_sdk_connect.types.number_comparison_type.serialize_json(
                value["comparison_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> NumberCondition:
    out: NumberCondition = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        out["field_name"] = data["FieldName"]
    if "MinValue" in data:
        out["min_value"] = data["MinValue"]
    if "MaxValue" in data:
        out["max_value"] = data["MaxValue"]
    if "ComparisonType" in data:
        import aws_sdk_connect.types.number_comparison_type

        out["comparison_type"] = (
            aws_sdk_connect.types.number_comparison_type.deserialize_json(
                data["ComparisonType"]
            )
        )
    return out
