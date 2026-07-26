"""Generated from Smithy shape ``com.amazonaws.opensearch#LogPublishingOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.log_publishing_option
    import capo_opensearch.types.log_type

LogPublishingOptions: TypeAlias = dict[
    "capo_opensearch.types.log_type.LogType",
    "capo_opensearch.types.log_publishing_option.LogPublishingOption",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LogPublishingOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_opensearch.types.log_publishing_option
        import capo_opensearch.types.log_type

        out[capo_opensearch.types.log_type.serialize_json(key)] = (
            capo_opensearch.types.log_publishing_option.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> LogPublishingOptions:
    out: LogPublishingOptions = {}
    for key, value in data.items():
        import capo_opensearch.types.log_publishing_option
        import capo_opensearch.types.log_type

        out[capo_opensearch.types.log_type.deserialize_json(key)] = (
            capo_opensearch.types.log_publishing_option.deserialize_json(value)
        )
    return out
