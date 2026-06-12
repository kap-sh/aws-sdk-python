"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SupplementalDataStorageLocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

SupplementalDataStorageLocationType: TypeAlias = Literal["S3",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("S3",))


def serialize_json(value: SupplementalDataStorageLocationType) -> str:
    return value


def deserialize_json(data: str) -> SupplementalDataStorageLocationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SupplementalDataStorageLocationType value: {data!r}"
        )
    return cast(SupplementalDataStorageLocationType, data)
