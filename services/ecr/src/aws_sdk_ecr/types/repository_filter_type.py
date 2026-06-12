"""Generated from Smithy shape ``com.amazonaws.ecr#RepositoryFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

RepositoryFilterType: TypeAlias = Literal["PREFIX_MATCH",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PREFIX_MATCH",))


def serialize_aws_json_1_1(value: RepositoryFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RepositoryFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RepositoryFilterType value: {data!r}")
    return cast(RepositoryFilterType, data)
