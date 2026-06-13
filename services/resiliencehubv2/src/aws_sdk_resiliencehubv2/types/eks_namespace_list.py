"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EksNamespaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.eks_namespace

EksNamespaceList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.eks_namespace.EksNamespace"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksNamespaceList) -> list:
    return list(value)


def deserialize_json(data: list) -> EksNamespaceList:
    return list(data)
