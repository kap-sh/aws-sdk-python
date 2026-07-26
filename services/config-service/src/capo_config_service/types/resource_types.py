"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.string_with_char_limit256

ResourceTypes: TypeAlias = list[
    "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceTypes:
    return list(data)
