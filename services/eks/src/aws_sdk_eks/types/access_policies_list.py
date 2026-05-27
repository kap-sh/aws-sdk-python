"""Generated from Smithy shape ``com.amazonaws.eks#AccessPoliciesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.access_policy

AccessPoliciesList: TypeAlias = list["aws_sdk_eks.types.access_policy.AccessPolicy"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessPoliciesList) -> list:
    import aws_sdk_eks.types.access_policy

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.access_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessPoliciesList:
    import aws_sdk_eks.types.access_policy

    out: AccessPoliciesList = []
    for item in data:
        out.append(aws_sdk_eks.types.access_policy.deserialize_json(item))
    return out
