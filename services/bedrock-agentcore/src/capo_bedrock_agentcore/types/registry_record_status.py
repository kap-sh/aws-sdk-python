"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RegistryRecordStatus``."""

from typing import Literal, TypeAlias, cast

"""<p> The status of a registry record in its lifecycle.</p>"""
RegistryRecordStatus: TypeAlias = Literal[
    "DRAFT",
    "PENDING_APPROVAL",
    "APPROVED",
    "REJECTED",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordStatus) -> str:
    return value


def deserialize_json(data: str) -> RegistryRecordStatus:
    return cast(RegistryRecordStatus, data)
