"""Generated from Smithy shape ``com.amazonaws.ecr#ScanningConfigurationFailureCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

ScanningConfigurationFailureCode: TypeAlias = Literal["REPOSITORY_NOT_FOUND",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("REPOSITORY_NOT_FOUND",))


def serialize_aws_json_1_1(value: ScanningConfigurationFailureCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScanningConfigurationFailureCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ScanningConfigurationFailureCode value: {data!r}"
        )
    return cast(ScanningConfigurationFailureCode, data)
