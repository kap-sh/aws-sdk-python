"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.ocsf_string_filter

OcsfStringFilterList: TypeAlias = list[
    "capo_securityhub.types.ocsf_string_filter.OcsfStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfStringFilterList) -> list:
    import capo_securityhub.types.ocsf_string_filter

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.ocsf_string_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> OcsfStringFilterList:
    import capo_securityhub.types.ocsf_string_filter

    out: OcsfStringFilterList = []
    for item in data:
        out.append(capo_securityhub.types.ocsf_string_filter.deserialize_json(item))
    return out
