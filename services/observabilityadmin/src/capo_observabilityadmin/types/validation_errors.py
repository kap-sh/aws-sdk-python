"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ValidationErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.validation_error

ValidationErrors: TypeAlias = list[
    "capo_observabilityadmin.types.validation_error.ValidationError"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationErrors) -> list:
    import capo_observabilityadmin.types.validation_error

    out: list = []
    for item in value:
        out.append(capo_observabilityadmin.types.validation_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValidationErrors:
    import capo_observabilityadmin.types.validation_error

    out: ValidationErrors = []
    for item in data:
        out.append(
            capo_observabilityadmin.types.validation_error.deserialize_json(item)
        )
    return out
