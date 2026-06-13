"""Generated from Smithy shape ``com.amazonaws.quicksight#Parameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.date_time_parameter_list
    import aws_sdk_quicksight.types.decimal_parameter_list
    import aws_sdk_quicksight.types.integer_parameter_list
    import aws_sdk_quicksight.types.string_parameter_list


class Parameters(TypedDict):
    string_parameters: NotRequired[
        "aws_sdk_quicksight.types.string_parameter_list.StringParameterList"
    ]
    """<p>The parameters that have a data type of string.</p>"""
    integer_parameters: NotRequired[
        "aws_sdk_quicksight.types.integer_parameter_list.IntegerParameterList"
    ]
    """<p>The parameters that have a data type of integer.</p>"""
    decimal_parameters: NotRequired[
        "aws_sdk_quicksight.types.decimal_parameter_list.DecimalParameterList"
    ]
    """<p>The parameters that have a data type of decimal.</p>"""
    date_time_parameters: NotRequired[
        "aws_sdk_quicksight.types.date_time_parameter_list.DateTimeParameterList"
    ]
    """<p>The parameters that have a data type of date-time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Parameters) -> dict:
    out: dict = {}
    if "string_parameters" in value:
        import aws_sdk_quicksight.types.string_parameter_list

        out["StringParameters"] = (
            aws_sdk_quicksight.types.string_parameter_list.serialize_json(
                value["string_parameters"]
            )
        )
    if "integer_parameters" in value:
        import aws_sdk_quicksight.types.integer_parameter_list

        out["IntegerParameters"] = (
            aws_sdk_quicksight.types.integer_parameter_list.serialize_json(
                value["integer_parameters"]
            )
        )
    if "decimal_parameters" in value:
        import aws_sdk_quicksight.types.decimal_parameter_list

        out["DecimalParameters"] = (
            aws_sdk_quicksight.types.decimal_parameter_list.serialize_json(
                value["decimal_parameters"]
            )
        )
    if "date_time_parameters" in value:
        import aws_sdk_quicksight.types.date_time_parameter_list

        out["DateTimeParameters"] = (
            aws_sdk_quicksight.types.date_time_parameter_list.serialize_json(
                value["date_time_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> Parameters:
    out: Parameters = {}  # type: ignore[typeddict-item]
    if "StringParameters" in data:
        import aws_sdk_quicksight.types.string_parameter_list

        out["string_parameters"] = (
            aws_sdk_quicksight.types.string_parameter_list.deserialize_json(
                data["StringParameters"]
            )
        )
    if "IntegerParameters" in data:
        import aws_sdk_quicksight.types.integer_parameter_list

        out["integer_parameters"] = (
            aws_sdk_quicksight.types.integer_parameter_list.deserialize_json(
                data["IntegerParameters"]
            )
        )
    if "DecimalParameters" in data:
        import aws_sdk_quicksight.types.decimal_parameter_list

        out["decimal_parameters"] = (
            aws_sdk_quicksight.types.decimal_parameter_list.deserialize_json(
                data["DecimalParameters"]
            )
        )
    if "DateTimeParameters" in data:
        import aws_sdk_quicksight.types.date_time_parameter_list

        out["date_time_parameters"] = (
            aws_sdk_quicksight.types.date_time_parameter_list.deserialize_json(
                data["DateTimeParameters"]
            )
        )
    return out
