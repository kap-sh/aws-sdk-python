"""Generated from Smithy shape ``com.amazonaws.securitylake#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securitylake.types.tag

TagList: TypeAlias = list["capo_securitylake.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: TagList) -> list:
    import capo_securitylake.types.tag

    out: list = []
    for item in value:
        out.append(capo_securitylake.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagList:
    import capo_securitylake.types.tag

    out: TagList = []
    for item in data:
        out.append(capo_securitylake.types.tag.deserialize_json(item))
    return out
