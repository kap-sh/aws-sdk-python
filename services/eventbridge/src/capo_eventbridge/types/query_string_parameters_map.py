"""Generated from Smithy shape ``com.amazonaws.eventbridge#QueryStringParametersMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.query_string_key
    import capo_eventbridge.types.query_string_value

QueryStringParametersMap: TypeAlias = dict[
    "capo_eventbridge.types.query_string_key.QueryStringKey",
    "capo_eventbridge.types.query_string_value.QueryStringValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: QueryStringParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryStringParametersMap:
    out: QueryStringParametersMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
