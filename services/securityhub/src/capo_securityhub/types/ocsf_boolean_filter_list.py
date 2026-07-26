"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfBooleanFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.ocsf_boolean_filter

OcsfBooleanFilterList: TypeAlias = list[
    "capo_securityhub.types.ocsf_boolean_filter.OcsfBooleanFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfBooleanFilterList) -> list:
    import capo_securityhub.types.ocsf_boolean_filter

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.ocsf_boolean_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> OcsfBooleanFilterList:
    import capo_securityhub.types.ocsf_boolean_filter

    out: OcsfBooleanFilterList = []
    for item in data:
        out.append(capo_securityhub.types.ocsf_boolean_filter.deserialize_json(item))
    return out
