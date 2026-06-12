"""Generated from Smithy shape ``com.amazonaws.sesv2#ReputationEntityFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.reputation_entity_filter_key
    import aws_sdk_sesv2.types.reputation_entity_filter_value

ReputationEntityFilter: TypeAlias = dict[
    "aws_sdk_sesv2.types.reputation_entity_filter_key.ReputationEntityFilterKey",
    "aws_sdk_sesv2.types.reputation_entity_filter_value.ReputationEntityFilterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ReputationEntityFilter) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sesv2.types.reputation_entity_filter_key

        out[aws_sdk_sesv2.types.reputation_entity_filter_key.serialize_json(key)] = (
            value
        )
    return out


def deserialize_json(data: dict) -> ReputationEntityFilter:
    out: ReputationEntityFilter = {}
    for key, value in data.items():
        import aws_sdk_sesv2.types.reputation_entity_filter_key

        out[aws_sdk_sesv2.types.reputation_entity_filter_key.deserialize_json(key)] = (
            value
        )
    return out
