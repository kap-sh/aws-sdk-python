"""Generated from Smithy shape ``com.amazonaws.configservice#Owner``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

Owner: TypeAlias = Literal[
    "CUSTOM_LAMBDA",
    "AWS",
    "CUSTOM_POLICY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM_LAMBDA",
        "AWS",
        "CUSTOM_POLICY",
    )
)


def serialize_aws_json_1_1(value: Owner) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Owner:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Owner value: {data!r}")
    return cast(Owner, data)
