"""Generated from Smithy shape ``com.amazonaws.groundstation#ContactVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.contact_version

ContactVersionsList: TypeAlias = list[
    "capo_groundstation.types.contact_version.ContactVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactVersionsList) -> list:
    import capo_groundstation.types.contact_version

    out: list = []
    for item in value:
        out.append(capo_groundstation.types.contact_version.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactVersionsList:
    import capo_groundstation.types.contact_version

    out: ContactVersionsList = []
    for item in data:
        out.append(capo_groundstation.types.contact_version.deserialize_json(item))
    return out
