"""Generated from Smithy shape ``com.amazonaws.outposts#OrderingRequirementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.ordering_requirement

OrderingRequirementList: TypeAlias = list[
    "aws_sdk_outposts.types.ordering_requirement.OrderingRequirement"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderingRequirementList) -> list:
    import aws_sdk_outposts.types.ordering_requirement

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.ordering_requirement.serialize_json(item))
    return out


def deserialize_json(data: list) -> OrderingRequirementList:
    import aws_sdk_outposts.types.ordering_requirement

    out: OrderingRequirementList = []
    for item in data:
        out.append(aws_sdk_outposts.types.ordering_requirement.deserialize_json(item))
    return out
