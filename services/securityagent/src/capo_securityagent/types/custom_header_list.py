"""Generated from Smithy shape ``com.amazonaws.securityagent#CustomHeaderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.custom_header

CustomHeaderList: TypeAlias = list[
    "capo_securityagent.types.custom_header.CustomHeader"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomHeaderList) -> list:
    import capo_securityagent.types.custom_header

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.custom_header.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomHeaderList:
    import capo_securityagent.types.custom_header

    out: CustomHeaderList = []
    for item in data:
        out.append(capo_securityagent.types.custom_header.deserialize_json(item))
    return out
