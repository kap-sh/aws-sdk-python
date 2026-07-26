"""Generated from Smithy shape ``com.amazonaws.securitylake#OcsfEventClassList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securitylake.types.ocsf_event_class

OcsfEventClassList: TypeAlias = list[
    "capo_securitylake.types.ocsf_event_class.OcsfEventClass"
]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfEventClassList) -> list:
    return list(value)


def deserialize_json(data: list) -> OcsfEventClassList:
    return list(data)
