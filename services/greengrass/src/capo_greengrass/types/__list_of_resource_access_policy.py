"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfResourceAccessPolicy``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrass.types.resource_access_policy

__listOfResourceAccessPolicy: TypeAlias = list[
    "capo_greengrass.types.resource_access_policy.ResourceAccessPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfResourceAccessPolicy) -> list:
    import capo_greengrass.types.resource_access_policy

    out: list = []
    for item in value:
        out.append(capo_greengrass.types.resource_access_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfResourceAccessPolicy:
    import capo_greengrass.types.resource_access_policy

    out: __listOfResourceAccessPolicy = []
    for item in data:
        out.append(capo_greengrass.types.resource_access_policy.deserialize_json(item))
    return out
