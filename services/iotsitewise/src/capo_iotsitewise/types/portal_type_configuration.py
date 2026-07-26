"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PortalTypeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.portal_type_entry
    import capo_iotsitewise.types.portal_type_key

PortalTypeConfiguration: TypeAlias = dict[
    "capo_iotsitewise.types.portal_type_key.PortalTypeKey",
    "capo_iotsitewise.types.portal_type_entry.PortalTypeEntry",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PortalTypeConfiguration) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iotsitewise.types.portal_type_entry

        out[key] = capo_iotsitewise.types.portal_type_entry.serialize_json(value)
    return out


def deserialize_json(data: dict) -> PortalTypeConfiguration:
    out: PortalTypeConfiguration = {}
    for key, value in data.items():
        import capo_iotsitewise.types.portal_type_entry

        out[key] = capo_iotsitewise.types.portal_type_entry.deserialize_json(value)
    return out
