"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_policy_detail

LifecyclePolicyDetails: TypeAlias = list[
    "aws_sdk_imagebuilder.types.lifecycle_policy_detail.LifecyclePolicyDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyDetails) -> list:
    import aws_sdk_imagebuilder.types.lifecycle_policy_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.lifecycle_policy_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LifecyclePolicyDetails:
    import aws_sdk_imagebuilder.types.lifecycle_policy_detail

    out: LifecyclePolicyDetails = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.lifecycle_policy_detail.deserialize_json(item)
        )
    return out
