"""Generated from Smithy shape ``com.amazonaws.connect#ValidationTestTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.validation_test_type

ValidationTestTypes: TypeAlias = list[
    "capo_connect.types.validation_test_type.ValidationTestType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationTestTypes) -> list:
    return list(value)


def deserialize_json(data: list) -> ValidationTestTypes:
    return list(data)
