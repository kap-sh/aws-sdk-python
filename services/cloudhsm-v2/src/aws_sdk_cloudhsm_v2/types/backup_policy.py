"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#BackupPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudhsm_v2.errors import DeserializationError

BackupPolicy: TypeAlias = Literal["DEFAULT",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DEFAULT",))


def serialize_aws_json_1_1(value: BackupPolicy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BackupPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BackupPolicy value: {data!r}")
    return cast(BackupPolicy, data)
