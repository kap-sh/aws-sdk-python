"""Generated from Smithy shape ``com.amazonaws.quicksight#FormatConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.date_time_format_configuration
    import aws_sdk_quicksight.types.number_format_configuration
    import aws_sdk_quicksight.types.string_format_configuration


class FormatConfiguration(TypedDict):
    string_format_configuration: NotRequired[
        "aws_sdk_quicksight.types.string_format_configuration.StringFormatConfiguration"
    ]
    """<p>Formatting configuration for string fields.</p>"""
    number_format_configuration: NotRequired[
        "aws_sdk_quicksight.types.number_format_configuration.NumberFormatConfiguration"
    ]
    """<p>Formatting configuration for number fields.</p>"""
    date_time_format_configuration: NotRequired[
        "aws_sdk_quicksight.types.date_time_format_configuration.DateTimeFormatConfiguration"
    ]
    """<p>Formatting configuration for <code>DateTime</code> fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormatConfiguration) -> dict:
    out: dict = {}
    if "string_format_configuration" in value:
        import aws_sdk_quicksight.types.string_format_configuration

        out["StringFormatConfiguration"] = (
            aws_sdk_quicksight.types.string_format_configuration.serialize_json(
                value["string_format_configuration"]
            )
        )
    if "number_format_configuration" in value:
        import aws_sdk_quicksight.types.number_format_configuration

        out["NumberFormatConfiguration"] = (
            aws_sdk_quicksight.types.number_format_configuration.serialize_json(
                value["number_format_configuration"]
            )
        )
    if "date_time_format_configuration" in value:
        import aws_sdk_quicksight.types.date_time_format_configuration

        out["DateTimeFormatConfiguration"] = (
            aws_sdk_quicksight.types.date_time_format_configuration.serialize_json(
                value["date_time_format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> FormatConfiguration:
    out: FormatConfiguration = {}  # type: ignore[typeddict-item]
    if "StringFormatConfiguration" in data:
        import aws_sdk_quicksight.types.string_format_configuration

        out["string_format_configuration"] = (
            aws_sdk_quicksight.types.string_format_configuration.deserialize_json(
                data["StringFormatConfiguration"]
            )
        )
    if "NumberFormatConfiguration" in data:
        import aws_sdk_quicksight.types.number_format_configuration

        out["number_format_configuration"] = (
            aws_sdk_quicksight.types.number_format_configuration.deserialize_json(
                data["NumberFormatConfiguration"]
            )
        )
    if "DateTimeFormatConfiguration" in data:
        import aws_sdk_quicksight.types.date_time_format_configuration

        out["date_time_format_configuration"] = (
            aws_sdk_quicksight.types.date_time_format_configuration.deserialize_json(
                data["DateTimeFormatConfiguration"]
            )
        )
    return out
