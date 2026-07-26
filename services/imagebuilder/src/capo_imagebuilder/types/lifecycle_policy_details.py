"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.lifecycle_policy_detail

LifecyclePolicyDetails: TypeAlias = list[
    "capo_imagebuilder.types.lifecycle_policy_detail.LifecyclePolicyDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyDetails) -> list:
    import capo_imagebuilder.types.lifecycle_policy_detail

    out: list = []
    for item in value:
        out.append(capo_imagebuilder.types.lifecycle_policy_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> LifecyclePolicyDetails:
    import capo_imagebuilder.types.lifecycle_policy_detail

    out: LifecyclePolicyDetails = []
    for item in data:
        out.append(
            capo_imagebuilder.types.lifecycle_policy_detail.deserialize_json(item)
        )
    return out
