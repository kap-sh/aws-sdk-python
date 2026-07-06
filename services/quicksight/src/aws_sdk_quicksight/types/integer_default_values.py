"""Generated from Smithy shape ``com.amazonaws.quicksight#IntegerDefaultValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dynamic_default_value
    import aws_sdk_quicksight.types.integer_default_value_list


class IntegerDefaultValues(TypedDict, closed=True):
    dynamic_value: NotRequired[
        "aws_sdk_quicksight.types.dynamic_default_value.DynamicDefaultValue"
    ]
    """<p>The dynamic value of the <code>IntegerDefaultValues</code>. Different defaults are displayed according to users, groups, and values mapping.</p>"""
    static_values: NotRequired[
        "aws_sdk_quicksight.types.integer_default_value_list.IntegerDefaultValueList"
    ]
    """<p>The static values of the <code>IntegerDefaultValues</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegerDefaultValues) -> dict:
    out: dict = {}
    if "dynamic_value" in value:
        import aws_sdk_quicksight.types.dynamic_default_value

        out["DynamicValue"] = (
            aws_sdk_quicksight.types.dynamic_default_value.serialize_json(
                value["dynamic_value"]
            )
        )
    if "static_values" in value:
        import aws_sdk_quicksight.types.integer_default_value_list

        out["StaticValues"] = (
            aws_sdk_quicksight.types.integer_default_value_list.serialize_json(
                value["static_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntegerDefaultValues:
    out: IntegerDefaultValues = {}  # type: ignore[typeddict-item]
    if "DynamicValue" in data:
        import aws_sdk_quicksight.types.dynamic_default_value

        out["dynamic_value"] = (
            aws_sdk_quicksight.types.dynamic_default_value.deserialize_json(
                data["DynamicValue"]
            )
        )
    if "StaticValues" in data:
        import aws_sdk_quicksight.types.integer_default_value_list

        out["static_values"] = (
            aws_sdk_quicksight.types.integer_default_value_list.deserialize_json(
                data["StaticValues"]
            )
        )
    return out
