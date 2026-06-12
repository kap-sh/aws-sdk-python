"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#LogPublishingOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.log_publishing_option
    import aws_sdk_elasticsearch_service.types.log_type

LogPublishingOptions: TypeAlias = dict[
    "aws_sdk_elasticsearch_service.types.log_type.LogType",
    "aws_sdk_elasticsearch_service.types.log_publishing_option.LogPublishingOption",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LogPublishingOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_elasticsearch_service.types.log_publishing_option
        import aws_sdk_elasticsearch_service.types.log_type

        out[aws_sdk_elasticsearch_service.types.log_type.serialize_json(key)] = (
            aws_sdk_elasticsearch_service.types.log_publishing_option.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> LogPublishingOptions:
    out: LogPublishingOptions = {}
    for key, value in data.items():
        import aws_sdk_elasticsearch_service.types.log_publishing_option
        import aws_sdk_elasticsearch_service.types.log_type

        out[aws_sdk_elasticsearch_service.types.log_type.deserialize_json(key)] = (
            aws_sdk_elasticsearch_service.types.log_publishing_option.deserialize_json(
                value
            )
        )
    return out
