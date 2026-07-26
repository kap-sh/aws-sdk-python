"""Generated from Smithy shape ``com.amazonaws.schemas#__listOfRegistrySummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_schemas.types.registry_summary

__listOfRegistrySummary: TypeAlias = list[
    "capo_schemas.types.registry_summary.RegistrySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRegistrySummary) -> list:
    import capo_schemas.types.registry_summary

    out: list = []
    for item in value:
        out.append(capo_schemas.types.registry_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfRegistrySummary:
    import capo_schemas.types.registry_summary

    out: __listOfRegistrySummary = []
    for item in data:
        out.append(capo_schemas.types.registry_summary.deserialize_json(item))
    return out
