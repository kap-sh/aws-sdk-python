"""Generated from Smithy shape ``com.amazonaws.appsync#ApiKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appsync.types.api_key

ApiKeys: TypeAlias = list["capo_appsync.types.api_key.ApiKey"]


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeys) -> list:
    import capo_appsync.types.api_key

    out: list = []
    for item in value:
        out.append(capo_appsync.types.api_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApiKeys:
    import capo_appsync.types.api_key

    out: ApiKeys = []
    for item in data:
        out.append(capo_appsync.types.api_key.deserialize_json(item))
    return out
