"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncS3Format``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ResourceDataSyncS3Format: TypeAlias = Literal["JsonSerDe",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("JsonSerDe",))


def serialize_aws_json_1_1(value: ResourceDataSyncS3Format) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceDataSyncS3Format:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceDataSyncS3Format value: {data!r}")
    return cast(ResourceDataSyncS3Format, data)
