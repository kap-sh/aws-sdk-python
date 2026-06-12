"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ExportDataFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

ExportDataFormat: TypeAlias = Literal["CSV",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CSV",))


def serialize_aws_json_1_1(value: ExportDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExportDataFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportDataFormat value: {data!r}")
    return cast(ExportDataFormat, data)
