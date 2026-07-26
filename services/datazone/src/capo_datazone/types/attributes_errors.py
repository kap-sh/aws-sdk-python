"""Generated from Smithy shape ``com.amazonaws.datazone#AttributesErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.attribute_error

AttributesErrors: TypeAlias = list["capo_datazone.types.attribute_error.AttributeError"]


# --- restJson1 ser/de ---
def serialize_json(value: AttributesErrors) -> list:
    import capo_datazone.types.attribute_error

    out: list = []
    for item in value:
        out.append(capo_datazone.types.attribute_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttributesErrors:
    import capo_datazone.types.attribute_error

    out: AttributesErrors = []
    for item in data:
        out.append(capo_datazone.types.attribute_error.deserialize_json(item))
    return out
