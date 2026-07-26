"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfMapField``."""

from typing import Literal, TypeAlias, cast

OcsfMapField: TypeAlias = Literal[
    "resources.tags",
    "compliance.control_parameters",
    "databucket.tags",
    "finding_info.tags",
]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfMapField) -> str:
    return value


def deserialize_json(data: str) -> OcsfMapField:
    return cast(OcsfMapField, data)
