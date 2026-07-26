"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfAddressConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.address_configuration

MapOfAddressConfiguration: TypeAlias = dict[
    "capo_pinpoint.types.__string.__string",
    "capo_pinpoint.types.address_configuration.AddressConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfAddressConfiguration) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_pinpoint.types.address_configuration

        out[key] = capo_pinpoint.types.address_configuration.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfAddressConfiguration:
    out: MapOfAddressConfiguration = {}
    for key, value in data.items():
        import capo_pinpoint.types.address_configuration

        out[key] = capo_pinpoint.types.address_configuration.deserialize_json(value)
    return out
