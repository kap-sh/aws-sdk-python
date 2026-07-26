"""Generated from Smithy shape ``com.amazonaws.securityhub#Standards``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.standard

Standards: TypeAlias = list["capo_securityhub.types.standard.Standard"]


# --- restJson1 ser/de ---
def serialize_json(value: Standards) -> list:
    import capo_securityhub.types.standard

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.standard.serialize_json(item))
    return out


def deserialize_json(data: list) -> Standards:
    import capo_securityhub.types.standard

    out: Standards = []
    for item in data:
        out.append(capo_securityhub.types.standard.deserialize_json(item))
    return out
