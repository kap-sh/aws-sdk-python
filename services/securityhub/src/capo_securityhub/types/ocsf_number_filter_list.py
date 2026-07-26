"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfNumberFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.ocsf_number_filter

OcsfNumberFilterList: TypeAlias = list[
    "capo_securityhub.types.ocsf_number_filter.OcsfNumberFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfNumberFilterList) -> list:
    import capo_securityhub.types.ocsf_number_filter

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.ocsf_number_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> OcsfNumberFilterList:
    import capo_securityhub.types.ocsf_number_filter

    out: OcsfNumberFilterList = []
    for item in data:
        out.append(capo_securityhub.types.ocsf_number_filter.deserialize_json(item))
    return out
