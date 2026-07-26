"""Generated from Smithy shape ``com.amazonaws.connect#AllowedExtensionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.allowed_extension

AllowedExtensionsList: TypeAlias = list[
    "capo_connect.types.allowed_extension.AllowedExtension"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedExtensionsList) -> list:
    import capo_connect.types.allowed_extension

    out: list = []
    for item in value:
        out.append(capo_connect.types.allowed_extension.serialize_json(item))
    return out


def deserialize_json(data: list) -> AllowedExtensionsList:
    import capo_connect.types.allowed_extension

    out: AllowedExtensionsList = []
    for item in data:
        out.append(capo_connect.types.allowed_extension.deserialize_json(item))
    return out
