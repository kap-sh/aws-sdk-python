"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#Exprs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.string

Exprs: TypeAlias = dict[
    "aws_sdk_cloudsearch_domain.types.string.String",
    "aws_sdk_cloudsearch_domain.types.string.String",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Exprs) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Exprs:
    out: Exprs = {}
    for key, value in data.items():
        out[key] = value
    return out
