"""Generated from Smithy shape ``com.amazonaws.osis#ValidationMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_osis.types.validation_message

ValidationMessageList: TypeAlias = list[
    "capo_osis.types.validation_message.ValidationMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationMessageList) -> list:
    import capo_osis.types.validation_message

    out: list = []
    for item in value:
        out.append(capo_osis.types.validation_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValidationMessageList:
    import capo_osis.types.validation_message

    out: ValidationMessageList = []
    for item in data:
        out.append(capo_osis.types.validation_message.deserialize_json(item))
    return out
