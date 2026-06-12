"""Generated from Smithy shape ``com.amazonaws.lightsail#CloudFormationStackRecordSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

CloudFormationStackRecordSourceType: TypeAlias = Literal["ExportSnapshotRecord",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ExportSnapshotRecord",))


def serialize_aws_json_1_1(value: CloudFormationStackRecordSourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CloudFormationStackRecordSourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CloudFormationStackRecordSourceType value: {data!r}"
        )
    return cast(CloudFormationStackRecordSourceType, data)
