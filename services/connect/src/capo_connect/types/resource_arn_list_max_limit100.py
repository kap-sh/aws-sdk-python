"""Generated from Smithy shape ``com.amazonaws.connect#resourceArnListMaxLimit100``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.arn

resourceArnListMaxLimit100: TypeAlias = list["capo_connect.types.arn.ARN"]


# --- restJson1 ser/de ---
def serialize_json(value: resourceArnListMaxLimit100) -> list:
    return list(value)


def deserialize_json(data: list) -> resourceArnListMaxLimit100:
    return list(data)
