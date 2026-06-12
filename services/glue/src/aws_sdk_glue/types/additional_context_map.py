"""Generated from Smithy shape ``com.amazonaws.glue#AdditionalContextMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.context_key
    import aws_sdk_glue.types.context_value

AdditionalContextMap: TypeAlias = dict[
    "aws_sdk_glue.types.context_key.ContextKey",
    "aws_sdk_glue.types.context_value.ContextValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AdditionalContextMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> AdditionalContextMap:
    out: AdditionalContextMap = {}
    for key, value in data.items():
        out[key] = value
    return out
