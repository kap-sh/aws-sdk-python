"""Generated from Smithy shape ``com.amazonaws.applicationinsights#UpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

UpdateStatus: TypeAlias = Literal["RESOLVED",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RESOLVED",))


def serialize_aws_json_1_1(value: UpdateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateStatus value: {data!r}")
    return cast(UpdateStatus, data)
