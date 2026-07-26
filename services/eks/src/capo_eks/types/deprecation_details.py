"""Generated from Smithy shape ``com.amazonaws.eks#DeprecationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.deprecation_detail

DeprecationDetails: TypeAlias = list[
    "capo_eks.types.deprecation_detail.DeprecationDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeprecationDetails) -> list:
    import capo_eks.types.deprecation_detail

    out: list = []
    for item in value:
        out.append(capo_eks.types.deprecation_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeprecationDetails:
    import capo_eks.types.deprecation_detail

    out: DeprecationDetails = []
    for item in data:
        out.append(capo_eks.types.deprecation_detail.deserialize_json(item))
    return out
