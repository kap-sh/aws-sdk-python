"""Generated from Smithy shape ``com.amazonaws.quicksight#StringFormatConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.null_value_format_configuration
    import aws_sdk_quicksight.types.numeric_format_configuration


class StringFormatConfiguration(TypedDict):
    null_value_format_configuration: NotRequired[
        "aws_sdk_quicksight.types.null_value_format_configuration.NullValueFormatConfiguration"
    ]
    """<p>The options that determine the null value format configuration.</p>"""
    numeric_format_configuration: NotRequired[
        "aws_sdk_quicksight.types.numeric_format_configuration.NumericFormatConfiguration"
    ]
    """<p>The formatting configuration for numeric strings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringFormatConfiguration) -> dict:
    out: dict = {}
    if "null_value_format_configuration" in value:
        import aws_sdk_quicksight.types.null_value_format_configuration

        out["NullValueFormatConfiguration"] = (
            aws_sdk_quicksight.types.null_value_format_configuration.serialize_json(
                value["null_value_format_configuration"]
            )
        )
    if "numeric_format_configuration" in value:
        import aws_sdk_quicksight.types.numeric_format_configuration

        out["NumericFormatConfiguration"] = (
            aws_sdk_quicksight.types.numeric_format_configuration.serialize_json(
                value["numeric_format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StringFormatConfiguration:
    out: StringFormatConfiguration = {}  # type: ignore[typeddict-item]
    if "NullValueFormatConfiguration" in data:
        import aws_sdk_quicksight.types.null_value_format_configuration

        out["null_value_format_configuration"] = (
            aws_sdk_quicksight.types.null_value_format_configuration.deserialize_json(
                data["NullValueFormatConfiguration"]
            )
        )
    if "NumericFormatConfiguration" in data:
        import aws_sdk_quicksight.types.numeric_format_configuration

        out["numeric_format_configuration"] = (
            aws_sdk_quicksight.types.numeric_format_configuration.deserialize_json(
                data["NumericFormatConfiguration"]
            )
        )
    return out
