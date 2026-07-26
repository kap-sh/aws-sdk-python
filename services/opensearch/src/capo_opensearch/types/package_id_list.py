"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageIDList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.package_id

PackageIDList: TypeAlias = list["capo_opensearch.types.package_id.PackageID"]


# --- restJson1 ser/de ---
def serialize_json(value: PackageIDList) -> list:
    return list(value)


def deserialize_json(data: list) -> PackageIDList:
    return list(data)
