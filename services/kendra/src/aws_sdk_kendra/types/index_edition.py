"""Generated from Smithy shape ``com.amazonaws.kendra#IndexEdition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

IndexEdition: TypeAlias = Literal[
    "DEVELOPER_EDITION",
    "ENTERPRISE_EDITION",
    "GEN_AI_ENTERPRISE_EDITION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEVELOPER_EDITION",
        "ENTERPRISE_EDITION",
        "GEN_AI_ENTERPRISE_EDITION",
    )
)


def serialize_aws_json_1_1(value: IndexEdition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IndexEdition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IndexEdition value: {data!r}")
    return cast(IndexEdition, data)
