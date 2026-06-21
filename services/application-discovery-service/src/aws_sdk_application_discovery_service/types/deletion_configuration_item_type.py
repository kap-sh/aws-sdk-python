"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DeletionConfigurationItemType``."""

from typing import Literal, TypeAlias, cast

DeletionConfigurationItemType: TypeAlias = Literal["SERVER",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletionConfigurationItemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeletionConfigurationItemType:
    return cast(DeletionConfigurationItemType, data)
