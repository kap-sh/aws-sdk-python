"""Generated from Smithy shape ``com.amazonaws.bedrock#Validators``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.validator

Validators: TypeAlias = list["capo_bedrock.types.validator.Validator"]


# --- restJson1 ser/de ---
def serialize_json(value: Validators) -> list:
    import capo_bedrock.types.validator

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.validator.serialize_json(item))
    return out


def deserialize_json(data: list) -> Validators:
    import capo_bedrock.types.validator

    out: Validators = []
    for item in data:
        out.append(capo_bedrock.types.validator.deserialize_json(item))
    return out
