"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundlePrincipalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.principal

AssetBundlePrincipalList: TypeAlias = list["capo_quicksight.types.principal.Principal"]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundlePrincipalList) -> list:
    return list(value)


def deserialize_json(data: list) -> AssetBundlePrincipalList:
    return list(data)
