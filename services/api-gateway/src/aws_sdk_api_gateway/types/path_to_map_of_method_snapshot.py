"""Generated from Smithy shape ``com.amazonaws.apigateway#PathToMapOfMethodSnapshot``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.map_of_method_snapshot
    import aws_sdk_api_gateway.types.string

PathToMapOfMethodSnapshot: TypeAlias = dict[
    "aws_sdk_api_gateway.types.string.String",
    "aws_sdk_api_gateway.types.map_of_method_snapshot.MapOfMethodSnapshot",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PathToMapOfMethodSnapshot) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_api_gateway.types.map_of_method_snapshot

        out[key] = aws_sdk_api_gateway.types.map_of_method_snapshot.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> PathToMapOfMethodSnapshot:
    out: PathToMapOfMethodSnapshot = {}
    for key, value in data.items():
        import aws_sdk_api_gateway.types.map_of_method_snapshot

        out[key] = aws_sdk_api_gateway.types.map_of_method_snapshot.deserialize_json(
            value
        )
    return out
