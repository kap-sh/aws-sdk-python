"""Generated from Smithy shape ``com.amazonaws.iot#UpdateDimensionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.dimension_arn
    import aws_sdk_iot.types.dimension_name
    import aws_sdk_iot.types.dimension_string_values
    import aws_sdk_iot.types.dimension_type
    import aws_sdk_iot.types.timestamp


class UpdateDimensionResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_iot.types.dimension_name.DimensionName"]
    """<p>A unique identifier for the dimension.</p>"""
    arn: NotRequired["aws_sdk_iot.types.dimension_arn.DimensionArn"]
    """<p>The Amazon Resource Name (ARN)of the created dimension.</p>"""
    type: NotRequired["aws_sdk_iot.types.dimension_type.DimensionType"]
    """<p>The type of the dimension.</p>"""
    string_values: NotRequired[
        "aws_sdk_iot.types.dimension_string_values.DimensionStringValues"
    ]
    """<p>The value or list of values used to scope the dimension. For example, for topic filters, this is the pattern used to match the MQTT topic name.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p>The date and time, in milliseconds since epoch, when the dimension was initially created.</p>"""
    last_modified_date: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p>The date and time, in milliseconds since epoch, when the dimension was most recently updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDimensionResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "type" in value:
        import aws_sdk_iot.types.dimension_type

        out["type"] = aws_sdk_iot.types.dimension_type.serialize_json(value["type"])
    if "string_values" in value:
        import aws_sdk_iot.types.dimension_string_values

        out["stringValues"] = aws_sdk_iot.types.dimension_string_values.serialize_json(
            value["string_values"]
        )
    if "creation_date" in value:
        import aws_sdk_iot.types.timestamp

        out["creationDate"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import aws_sdk_iot.types.timestamp

        out["lastModifiedDate"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["last_modified_date"]
        )
    return out


def deserialize_json(data: dict) -> UpdateDimensionResponse:
    out: UpdateDimensionResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "type" in data:
        import aws_sdk_iot.types.dimension_type

        out["type"] = aws_sdk_iot.types.dimension_type.deserialize_json(data["type"])
    if "stringValues" in data:
        import aws_sdk_iot.types.dimension_string_values

        out["string_values"] = (
            aws_sdk_iot.types.dimension_string_values.deserialize_json(
                data["stringValues"]
            )
        )
    if "creationDate" in data:
        import aws_sdk_iot.types.timestamp

        out["creation_date"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    if "lastModifiedDate" in data:
        import aws_sdk_iot.types.timestamp

        out["last_modified_date"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["lastModifiedDate"]
        )
    return out
