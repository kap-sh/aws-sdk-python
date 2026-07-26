"""Generated from Smithy shape ``com.amazonaws.panorama#ApplicationInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.application_instance

ApplicationInstances: TypeAlias = list[
    "capo_panorama.types.application_instance.ApplicationInstance"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationInstances) -> list:
    import capo_panorama.types.application_instance

    out: list = []
    for item in value:
        out.append(capo_panorama.types.application_instance.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationInstances:
    import capo_panorama.types.application_instance

    out: ApplicationInstances = []
    for item in data:
        out.append(capo_panorama.types.application_instance.deserialize_json(item))
    return out
