"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentPermissionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

DocumentPermissionType: TypeAlias = Literal["Share",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Share",))


def serialize_aws_json_1_1(value: DocumentPermissionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentPermissionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentPermissionType value: {data!r}")
    return cast(DocumentPermissionType, data)
