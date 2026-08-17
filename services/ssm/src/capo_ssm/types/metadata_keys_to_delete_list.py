"""Generated from Smithy shape ``com.amazonaws.ssm#MetadataKeysToDeleteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.metadata_key

MetadataKeysToDeleteList: TypeAlias = list["capo_ssm.types.metadata_key.MetadataKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetadataKeysToDeleteList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MetadataKeysToDeleteList:
    return [item for item in data if item is not None]
