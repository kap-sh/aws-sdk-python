"""Generated from Smithy shape ``com.amazonaws.eks#AssociatedAccessPoliciesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.associated_access_policy

AssociatedAccessPoliciesList: TypeAlias = list[
    "aws_sdk_eks.types.associated_access_policy.AssociatedAccessPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedAccessPoliciesList) -> list:
    import aws_sdk_eks.types.associated_access_policy

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.associated_access_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedAccessPoliciesList:
    import aws_sdk_eks.types.associated_access_policy

    out: AssociatedAccessPoliciesList = []
    for item in data:
        out.append(aws_sdk_eks.types.associated_access_policy.deserialize_json(item))
    return out
