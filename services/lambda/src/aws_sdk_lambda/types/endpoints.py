"""Generated from Smithy shape ``com.amazonaws.lambda#Endpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.end_point_type
    import aws_sdk_lambda.types.endpoint_lists

Endpoints: TypeAlias = dict[
    "aws_sdk_lambda.types.end_point_type.EndPointType",
    "aws_sdk_lambda.types.endpoint_lists.EndpointLists",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Endpoints) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_lambda.types.end_point_type
        import aws_sdk_lambda.types.endpoint_lists

        out[aws_sdk_lambda.types.end_point_type.serialize_json(key)] = (
            aws_sdk_lambda.types.endpoint_lists.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> Endpoints:
    out: Endpoints = {}
    for key, value in data.items():
        import aws_sdk_lambda.types.end_point_type
        import aws_sdk_lambda.types.endpoint_lists

        out[aws_sdk_lambda.types.end_point_type.deserialize_json(key)] = (
            aws_sdk_lambda.types.endpoint_lists.deserialize_json(value)
        )
    return out
