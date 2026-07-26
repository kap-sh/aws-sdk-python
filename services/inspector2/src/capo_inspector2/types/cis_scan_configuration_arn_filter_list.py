"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanConfigurationArnFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.cis_string_filter

CisScanConfigurationArnFilterList: TypeAlias = list[
    "capo_inspector2.types.cis_string_filter.CisStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CisScanConfigurationArnFilterList) -> list:
    import capo_inspector2.types.cis_string_filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.cis_string_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CisScanConfigurationArnFilterList:
    import capo_inspector2.types.cis_string_filter

    out: CisScanConfigurationArnFilterList = []
    for item in data:
        out.append(capo_inspector2.types.cis_string_filter.deserialize_json(item))
    return out
