"""Generated from Smithy shape ``com.amazonaws.lambda#CompatibleRuntimes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.runtime

CompatibleRuntimes: TypeAlias = list["capo_lambda.types.runtime.Runtime"]


# --- restJson1 ser/de ---
def serialize_json(value: CompatibleRuntimes) -> list:
    import capo_lambda.types.runtime

    out: list = []
    for item in value:
        out.append(capo_lambda.types.runtime.serialize_json(item))
    return out


def deserialize_json(data: list) -> CompatibleRuntimes:
    import capo_lambda.types.runtime

    out: CompatibleRuntimes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda.types.runtime.deserialize_json(item))
    return out
