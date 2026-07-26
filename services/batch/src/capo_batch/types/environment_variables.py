"""Generated from Smithy shape ``com.amazonaws.batch#EnvironmentVariables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.key_value_pair

EnvironmentVariables: TypeAlias = list["capo_batch.types.key_value_pair.KeyValuePair"]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentVariables) -> list:
    import capo_batch.types.key_value_pair

    out: list = []
    for item in value:
        out.append(capo_batch.types.key_value_pair.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnvironmentVariables:
    import capo_batch.types.key_value_pair

    out: EnvironmentVariables = []
    for item in data:
        out.append(capo_batch.types.key_value_pair.deserialize_json(item))
    return out
