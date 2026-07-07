"""Generated from Smithy shape ``com.amazonaws.databrew#DatasetParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.create_column
    import aws_sdk_databrew.types.datetime_options
    import aws_sdk_databrew.types.filter_expression
    import aws_sdk_databrew.types.parameter_type
    import aws_sdk_databrew.types.path_parameter_name


class DatasetParameter(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.path_parameter_name.PathParameterName"
    """<p>The name of the parameter that is used in the dataset's Amazon S3 path.</p>"""
    type: "aws_sdk_databrew.types.parameter_type.ParameterType"
    """<p>The type of the dataset parameter, can be one of a 'String', 'Number' or 'Datetime'.</p>"""
    datetime_options: NotRequired[
        "aws_sdk_databrew.types.datetime_options.DatetimeOptions"
    ]
    """<p>Additional parameter options such as a format and a timezone. Required for datetime parameters.</p>"""
    create_column: "aws_sdk_databrew.types.create_column.CreateColumn"
    """<p>Optional boolean value that defines whether the captured value of this parameter should be used to create a new column in a dataset.</p>"""
    filter: NotRequired["aws_sdk_databrew.types.filter_expression.FilterExpression"]
    """<p>The optional filter expression structure to apply additional matching criteria to the parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_databrew.types.parameter_type

    out["Type"] = aws_sdk_databrew.types.parameter_type.serialize_json(value["type"])
    if "datetime_options" in value:
        import aws_sdk_databrew.types.datetime_options

        out["DatetimeOptions"] = aws_sdk_databrew.types.datetime_options.serialize_json(
            value["datetime_options"]
        )
    out["CreateColumn"] = value.get("create_column", False)
    if "filter" in value:
        import aws_sdk_databrew.types.filter_expression

        out["Filter"] = aws_sdk_databrew.types.filter_expression.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> DatasetParameter:
    out: DatasetParameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DatasetParameter.name required")
    if "Type" in data:
        import aws_sdk_databrew.types.parameter_type

        out["type"] = aws_sdk_databrew.types.parameter_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("DatasetParameter.type required")
    if "DatetimeOptions" in data:
        import aws_sdk_databrew.types.datetime_options

        out["datetime_options"] = (
            aws_sdk_databrew.types.datetime_options.deserialize_json(
                data["DatetimeOptions"]
            )
        )
    if "CreateColumn" in data:
        out["create_column"] = data["CreateColumn"]
    else:
        out["create_column"] = False
    if "Filter" in data:
        import aws_sdk_databrew.types.filter_expression

        out["filter"] = aws_sdk_databrew.types.filter_expression.deserialize_json(
            data["Filter"]
        )
    return out
