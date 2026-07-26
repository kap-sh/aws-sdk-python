"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ValidationErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_validation_error

ValidationErrorList: TypeAlias = list[
    "capo_socialmessaging.types.meta_flow_validation_error.MetaFlowValidationError"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationErrorList) -> list:
    return list(value)


def deserialize_json(data: list) -> ValidationErrorList:
    return list(data)
