"""Generated from Smithy shape ``com.amazonaws.quicksight#DecimalDefaultValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.decimal_default_value_list
    import aws_sdk_quicksight.types.dynamic_default_value


class DecimalDefaultValues(TypedDict, closed=True):
    dynamic_value: NotRequired[
        "aws_sdk_quicksight.types.dynamic_default_value.DynamicDefaultValue"
    ]
    """<p>The dynamic value of the <code>DecimalDefaultValues</code>. Different defaults are displayed according to users, groups, and values mapping.</p>"""
    static_values: NotRequired[
        "aws_sdk_quicksight.types.decimal_default_value_list.DecimalDefaultValueList"
    ]
    """<p>The static values of the <code>DecimalDefaultValues</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecimalDefaultValues) -> dict:
    out: dict = {}
    if "dynamic_value" in value:
        import aws_sdk_quicksight.types.dynamic_default_value

        out["DynamicValue"] = (
            aws_sdk_quicksight.types.dynamic_default_value.serialize_json(
                value["dynamic_value"]
            )
        )
    if "static_values" in value:
        import aws_sdk_quicksight.types.decimal_default_value_list

        out["StaticValues"] = (
            aws_sdk_quicksight.types.decimal_default_value_list.serialize_json(
                value["static_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> DecimalDefaultValues:
    out: DecimalDefaultValues = {}  # type: ignore[typeddict-item]
    if "DynamicValue" in data:
        import aws_sdk_quicksight.types.dynamic_default_value

        out["dynamic_value"] = (
            aws_sdk_quicksight.types.dynamic_default_value.deserialize_json(
                data["DynamicValue"]
            )
        )
    if "StaticValues" in data:
        import aws_sdk_quicksight.types.decimal_default_value_list

        out["static_values"] = (
            aws_sdk_quicksight.types.decimal_default_value_list.deserialize_json(
                data["StaticValues"]
            )
        )
    return out
