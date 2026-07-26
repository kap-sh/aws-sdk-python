"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfMapFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.ocsf_map_filter

OcsfMapFilterList: TypeAlias = list[
    "capo_securityhub.types.ocsf_map_filter.OcsfMapFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfMapFilterList) -> list:
    import capo_securityhub.types.ocsf_map_filter

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.ocsf_map_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> OcsfMapFilterList:
    import capo_securityhub.types.ocsf_map_filter

    out: OcsfMapFilterList = []
    for item in data:
        out.append(capo_securityhub.types.ocsf_map_filter.deserialize_json(item))
    return out
