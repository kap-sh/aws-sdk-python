"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#Filters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.strings

Filters: TypeAlias = dict["str", "capo_route53globalresolver.types.strings.Strings"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Filters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_route53globalresolver.types.strings

        out[key] = capo_route53globalresolver.types.strings.serialize_json(value)
    return out


def deserialize_json(data: dict) -> Filters:
    out: Filters = {}
    for key, value in data.items():
        import capo_route53globalresolver.types.strings

        out[key] = capo_route53globalresolver.types.strings.deserialize_json(value)
    return out
