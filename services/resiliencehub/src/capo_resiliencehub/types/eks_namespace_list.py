"""Generated from Smithy shape ``com.amazonaws.resiliencehub#EksNamespaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.eks_namespace

EksNamespaceList: TypeAlias = list[
    "capo_resiliencehub.types.eks_namespace.EksNamespace"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksNamespaceList) -> list:
    return list(value)


def deserialize_json(data: list) -> EksNamespaceList:
    return list(data)
