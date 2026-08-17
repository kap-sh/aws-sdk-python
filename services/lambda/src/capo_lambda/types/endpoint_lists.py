"""Generated from Smithy shape ``com.amazonaws.lambda#EndpointLists``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.endpoint

EndpointLists: TypeAlias = list["capo_lambda.types.endpoint.Endpoint"]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointLists) -> list:
    return list(value)


def deserialize_json(data: list) -> EndpointLists:
    return [item for item in data if item is not None]
