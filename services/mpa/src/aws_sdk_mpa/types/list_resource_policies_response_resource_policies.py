"""Generated from Smithy shape ``com.amazonaws.mpa#ListResourcePoliciesResponseResourcePolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mpa.types.list_resource_policies_response_resource_policy

ListResourcePoliciesResponseResourcePolicies: TypeAlias = list[
    "aws_sdk_mpa.types.list_resource_policies_response_resource_policy.ListResourcePoliciesResponseResourcePolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcePoliciesResponseResourcePolicies) -> list:
    import aws_sdk_mpa.types.list_resource_policies_response_resource_policy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mpa.types.list_resource_policies_response_resource_policy.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListResourcePoliciesResponseResourcePolicies:
    import aws_sdk_mpa.types.list_resource_policies_response_resource_policy

    out: ListResourcePoliciesResponseResourcePolicies = []
    for item in data:
        out.append(
            aws_sdk_mpa.types.list_resource_policies_response_resource_policy.deserialize_json(
                item
            )
        )
    return out
