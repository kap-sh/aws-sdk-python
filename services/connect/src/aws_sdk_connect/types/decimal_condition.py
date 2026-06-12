"""Generated from Smithy shape ``com.amazonaws.connect#DecimalCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.decimal_comparison_type
    import aws_sdk_connect.types.nullable_double
    import aws_sdk_connect.types.string


class DecimalCondition(TypedDict):
    field_name: NotRequired["aws_sdk_connect.types.string.String"]
    """<p>A name of the decimal property to be searched.</p>"""
    min_value: NotRequired["aws_sdk_connect.types.nullable_double.NullableDouble"]
    """<p>A minimum value of the decimal property.</p>"""
    max_value: NotRequired["aws_sdk_connect.types.nullable_double.NullableDouble"]
    """<p>A maximum value of the decimal property.</p>"""
    comparison_type: NotRequired[
        "aws_sdk_connect.types.decimal_comparison_type.DecimalComparisonType"
    ]
    """<p>The type of comparison to be made when evaluating the decimal condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecimalCondition) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    if "min_value" in value:
        out["MinValue"] = value["min_value"]
    if "max_value" in value:
        out["MaxValue"] = value["max_value"]
    if "comparison_type" in value:
        import aws_sdk_connect.types.decimal_comparison_type

        out["ComparisonType"] = (
            aws_sdk_connect.types.decimal_comparison_type.serialize_json(
                value["comparison_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DecimalCondition:
    out: DecimalCondition = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        out["field_name"] = data["FieldName"]
    if "MinValue" in data:
        out["min_value"] = data["MinValue"]
    if "MaxValue" in data:
        out["max_value"] = data["MaxValue"]
    if "ComparisonType" in data:
        import aws_sdk_connect.types.decimal_comparison_type

        out["comparison_type"] = (
            aws_sdk_connect.types.decimal_comparison_type.deserialize_json(
                data["ComparisonType"]
            )
        )
    return out
