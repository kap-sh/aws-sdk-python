"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ParameterMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.string
    import aws_sdk_timestream_query.types.type


class ParameterMapping(TypedDict, closed=True):
    name: "aws_sdk_timestream_query.types.string.String"
    """<p>Parameter name.</p>"""
    type: "aws_sdk_timestream_query.types.type.Type"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ParameterMapping) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_timestream_query.types.type

    out["Type"] = aws_sdk_timestream_query.types.type.serialize_aws_json_1_0(
        value["type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ParameterMapping:
    out: ParameterMapping = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ParameterMapping.name required")
    if "Type" in data:
        import aws_sdk_timestream_query.types.type

        out["type"] = aws_sdk_timestream_query.types.type.deserialize_aws_json_1_0(
            data["Type"]
        )
    else:
        raise DeserializationError("ParameterMapping.type required")
    return out
