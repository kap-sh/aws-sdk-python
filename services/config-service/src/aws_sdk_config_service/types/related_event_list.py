"""Generated from Smithy shape ``com.amazonaws.configservice#RelatedEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.related_event

RelatedEventList: TypeAlias = list[
    "aws_sdk_config_service.types.related_event.RelatedEvent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelatedEventList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RelatedEventList:
    return list(data)
