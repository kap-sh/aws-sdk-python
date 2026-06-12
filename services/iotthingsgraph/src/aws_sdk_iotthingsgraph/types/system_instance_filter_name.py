"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemInstanceFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotthingsgraph.errors import DeserializationError

SystemInstanceFilterName: TypeAlias = Literal[
    "SYSTEM_TEMPLATE_ID",
    "STATUS",
    "GREENGRASS_GROUP_NAME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SYSTEM_TEMPLATE_ID",
        "STATUS",
        "GREENGRASS_GROUP_NAME",
    )
)


def serialize_aws_json_1_1(value: SystemInstanceFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SystemInstanceFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SystemInstanceFilterName value: {data!r}")
    return cast(SystemInstanceFilterName, data)
