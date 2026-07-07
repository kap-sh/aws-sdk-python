"""Generated from Smithy shape ``com.amazonaws.iot#CreateDimensionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.client_request_token
    import aws_sdk_iot.types.dimension_name
    import aws_sdk_iot.types.dimension_string_values
    import aws_sdk_iot.types.dimension_type
    import aws_sdk_iot.types.tag_list


class CreateDimensionRequest(TypedDict, closed=True):
    name: "aws_sdk_iot.types.dimension_name.DimensionName"
    """<p>A unique identifier for the dimension. Choose something that describes the type and value to make it easy to remember what it does.</p>"""
    type: "aws_sdk_iot.types.dimension_type.DimensionType"
    """<p>Specifies the type of dimension. Supported types: <code>TOPIC_FILTER.</code> </p>"""
    string_values: "aws_sdk_iot.types.dimension_string_values.DimensionStringValues"
    r"""<p>Specifies the value or list of values for the dimension. For <code>TOPIC_FILTER</code> dimensions, this is a pattern used to match the MQTT topic (for example, \"admin/#\").</p>"""
    tags: NotRequired["aws_sdk_iot.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the dimension.</p>"""
    client_request_token: "aws_sdk_iot.types.client_request_token.ClientRequestToken"
    """<p>Each dimension must have a unique client request token. If you try to create a new dimension with the same token as a dimension that already exists, an exception occurs. If you omit this value, Amazon Web Services SDKs will automatically generate a unique client request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDimensionRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.dimension_type

    out["type"] = aws_sdk_iot.types.dimension_type.serialize_json(value["type"])
    import aws_sdk_iot.types.dimension_string_values

    out["stringValues"] = aws_sdk_iot.types.dimension_string_values.serialize_json(
        value["string_values"]
    )
    if "tags" in value:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.serialize_json(value["tags"])
    out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateDimensionRequest:
    out: CreateDimensionRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_iot.types.dimension_type

        out["type"] = aws_sdk_iot.types.dimension_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("CreateDimensionRequest.type required")
    if "stringValues" in data:
        import aws_sdk_iot.types.dimension_string_values

        out["string_values"] = (
            aws_sdk_iot.types.dimension_string_values.deserialize_json(
                data["stringValues"]
            )
        )
    else:
        raise DeserializationError("CreateDimensionRequest.string_values required")
    if "tags" in data:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.deserialize_json(data["tags"])
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    else:
        raise DeserializationError(
            "CreateDimensionRequest.client_request_token required"
        )
    return out
