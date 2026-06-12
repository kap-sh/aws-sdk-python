"""Generated from Smithy shape ``com.amazonaws.connect#BooleanCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.boolean_comparison_type
    import aws_sdk_connect.types.string


class BooleanCondition(TypedDict):
    field_name: NotRequired["aws_sdk_connect.types.string.String"]
    """<p>A name of the property to be searched.</p>"""
    comparison_type: NotRequired[
        "aws_sdk_connect.types.boolean_comparison_type.BooleanComparisonType"
    ]
    """<p>Boolean property comparison type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BooleanCondition) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    if "comparison_type" in value:
        import aws_sdk_connect.types.boolean_comparison_type

        out["ComparisonType"] = (
            aws_sdk_connect.types.boolean_comparison_type.serialize_json(
                value["comparison_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> BooleanCondition:
    out: BooleanCondition = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        out["field_name"] = data["FieldName"]
    if "ComparisonType" in data:
        import aws_sdk_connect.types.boolean_comparison_type

        out["comparison_type"] = (
            aws_sdk_connect.types.boolean_comparison_type.deserialize_json(
                data["ComparisonType"]
            )
        )
    return out
