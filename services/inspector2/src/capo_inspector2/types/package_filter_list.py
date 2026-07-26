"""Generated from Smithy shape ``com.amazonaws.inspector2#PackageFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.package_filter

PackageFilterList: TypeAlias = list[
    "capo_inspector2.types.package_filter.PackageFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageFilterList) -> list:
    import capo_inspector2.types.package_filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.package_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> PackageFilterList:
    import capo_inspector2.types.package_filter

    out: PackageFilterList = []
    for item in data:
        out.append(capo_inspector2.types.package_filter.deserialize_json(item))
    return out
