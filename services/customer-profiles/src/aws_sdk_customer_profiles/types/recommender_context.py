"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderContext``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.context_key
    import aws_sdk_customer_profiles.types.string1_to255

RecommenderContext: TypeAlias = dict[
    "aws_sdk_customer_profiles.types.context_key.ContextKey",
    "aws_sdk_customer_profiles.types.string1_to255.string1To255",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RecommenderContext) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> RecommenderContext:
    out: RecommenderContext = {}
    for key, value in data.items():
        out[key] = value
    return out
