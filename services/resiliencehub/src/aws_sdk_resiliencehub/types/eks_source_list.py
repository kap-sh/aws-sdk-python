"""Generated from Smithy shape ``com.amazonaws.resiliencehub#EksSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.eks_source

EksSourceList: TypeAlias = list["aws_sdk_resiliencehub.types.eks_source.EksSource"]


# --- restJson1 ser/de ---
def serialize_json(value: EksSourceList) -> list:
    import aws_sdk_resiliencehub.types.eks_source

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehub.types.eks_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> EksSourceList:
    import aws_sdk_resiliencehub.types.eks_source

    out: EksSourceList = []
    for item in data:
        out.append(aws_sdk_resiliencehub.types.eks_source.deserialize_json(item))
    return out
