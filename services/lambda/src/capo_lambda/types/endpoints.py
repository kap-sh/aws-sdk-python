"""Generated from Smithy shape ``com.amazonaws.lambda#Endpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.end_point_type
    import capo_lambda.types.endpoint_lists

Endpoints: TypeAlias = dict[
    "capo_lambda.types.end_point_type.EndPointType",
    "capo_lambda.types.endpoint_lists.EndpointLists",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Endpoints) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lambda.types.end_point_type
        import capo_lambda.types.endpoint_lists

        out[capo_lambda.types.end_point_type.serialize_json(key)] = (
            capo_lambda.types.endpoint_lists.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> Endpoints:
    out: Endpoints = {}
    for key, value in data.items():
        import capo_lambda.types.end_point_type

        if value is None:
            continue
        import capo_lambda.types.endpoint_lists

        out[capo_lambda.types.end_point_type.deserialize_json(key)] = (
            capo_lambda.types.endpoint_lists.deserialize_json(value)
        )
    return out
