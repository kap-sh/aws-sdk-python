"""Generated from Smithy shape ``com.amazonaws.mpa#ListResourcePoliciesResponseResourcePolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mpa.types.list_resource_policies_response_resource_policy

ListResourcePoliciesResponseResourcePolicies: TypeAlias = list[
    "capo_mpa.types.list_resource_policies_response_resource_policy.ListResourcePoliciesResponseResourcePolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcePoliciesResponseResourcePolicies) -> list:
    import capo_mpa.types.list_resource_policies_response_resource_policy

    out: list = []
    for item in value:
        out.append(
            capo_mpa.types.list_resource_policies_response_resource_policy.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListResourcePoliciesResponseResourcePolicies:
    import capo_mpa.types.list_resource_policies_response_resource_policy

    out: ListResourcePoliciesResponseResourcePolicies = []
    for item in data:
        out.append(
            capo_mpa.types.list_resource_policies_response_resource_policy.deserialize_json(
                item
            )
        )
    return out
