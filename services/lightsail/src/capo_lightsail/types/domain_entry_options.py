"""Generated from Smithy shape ``com.amazonaws.lightsail#DomainEntryOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.domain_entry_options_keys
    import capo_lightsail.types.string

DomainEntryOptions: TypeAlias = dict[
    "capo_lightsail.types.domain_entry_options_keys.DomainEntryOptionsKeys",
    "capo_lightsail.types.string.string",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: DomainEntryOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainEntryOptions:
    out: DomainEntryOptions = {}
    for key, value in data.items():
        out[key] = value
    return out
