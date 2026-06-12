"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResiliencyPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.resiliency_policy

ResiliencyPolicies: TypeAlias = list[
    "aws_sdk_resiliencehub.types.resiliency_policy.ResiliencyPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResiliencyPolicies) -> list:
    import aws_sdk_resiliencehub.types.resiliency_policy

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehub.types.resiliency_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResiliencyPolicies:
    import aws_sdk_resiliencehub.types.resiliency_policy

    out: ResiliencyPolicies = []
    for item in data:
        out.append(aws_sdk_resiliencehub.types.resiliency_policy.deserialize_json(item))
    return out
