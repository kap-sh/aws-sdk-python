"""Generated from Smithy shape ``com.amazonaws.ecr#ScanningRepositoryFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

ScanningRepositoryFilterType: TypeAlias = Literal["WILDCARD",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("WILDCARD",))


def serialize_aws_json_1_1(value: ScanningRepositoryFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScanningRepositoryFilterType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ScanningRepositoryFilterType value: {data!r}"
        )
    return cast(ScanningRepositoryFilterType, data)
