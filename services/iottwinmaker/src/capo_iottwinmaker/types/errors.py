"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#Errors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.batch_put_property_error

Errors: TypeAlias = list[
    "capo_iottwinmaker.types.batch_put_property_error.BatchPutPropertyError"
]


# --- restJson1 ser/de ---
def serialize_json(value: Errors) -> list:
    import capo_iottwinmaker.types.batch_put_property_error

    out: list = []
    for item in value:
        out.append(
            capo_iottwinmaker.types.batch_put_property_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> Errors:
    import capo_iottwinmaker.types.batch_put_property_error

    out: Errors = []
    for item in data:
        out.append(
            capo_iottwinmaker.types.batch_put_property_error.deserialize_json(item)
        )
    return out
