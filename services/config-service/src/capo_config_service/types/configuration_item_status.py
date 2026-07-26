"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationItemStatus``."""

from typing import Literal, TypeAlias, cast

ConfigurationItemStatus: TypeAlias = Literal[
    "OK",
    "ResourceDiscovered",
    "ResourceNotRecorded",
    "ResourceDeleted",
    "ResourceDeletedNotRecorded",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationItemStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigurationItemStatus:
    return cast(ConfigurationItemStatus, data)
