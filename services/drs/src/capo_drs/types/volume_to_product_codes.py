"""Generated from Smithy shape ``com.amazonaws.drs#VolumeToProductCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.large_bounded_string
    import capo_drs.types.product_codes

VolumeToProductCodes: TypeAlias = dict[
    "capo_drs.types.large_bounded_string.LargeBoundedString",
    "capo_drs.types.product_codes.ProductCodes",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: VolumeToProductCodes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_drs.types.product_codes

        out[key] = capo_drs.types.product_codes.serialize_json(value)
    return out


def deserialize_json(data: dict) -> VolumeToProductCodes:
    out: VolumeToProductCodes = {}
    for key, value in data.items():
        import capo_drs.types.product_codes

        out[key] = capo_drs.types.product_codes.deserialize_json(value)
    return out
