"""Generated from Smithy shape ``com.amazonaws.auditmanager#ExportDestinationType``."""

from typing import Literal, TypeAlias, cast

ExportDestinationType: TypeAlias = Literal["S3",]


# --- restJson1 ser/de ---
def serialize_json(value: ExportDestinationType) -> str:
    return value


def deserialize_json(data: str) -> ExportDestinationType:
    return cast(ExportDestinationType, data)
