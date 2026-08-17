"""Generated from Smithy shape ``com.amazonaws.eventbridge#HeaderParametersMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.header_key
    import capo_eventbridge.types.header_value

HeaderParametersMap: TypeAlias = dict[
    "capo_eventbridge.types.header_key.HeaderKey",
    "capo_eventbridge.types.header_value.HeaderValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: HeaderParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> HeaderParametersMap:
    out: HeaderParametersMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
