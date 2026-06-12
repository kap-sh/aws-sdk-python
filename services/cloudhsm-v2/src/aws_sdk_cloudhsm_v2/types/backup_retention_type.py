"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#BackupRetentionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudhsm_v2.errors import DeserializationError

BackupRetentionType: TypeAlias = Literal["DAYS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DAYS",))


def serialize_aws_json_1_1(value: BackupRetentionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BackupRetentionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BackupRetentionType value: {data!r}")
    return cast(BackupRetentionType, data)
