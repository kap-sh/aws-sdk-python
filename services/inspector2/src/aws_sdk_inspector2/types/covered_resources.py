"""Generated from Smithy shape ``com.amazonaws.inspector2#CoveredResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.covered_resource

CoveredResources: TypeAlias = list[
    "aws_sdk_inspector2.types.covered_resource.CoveredResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoveredResources) -> list:
    import aws_sdk_inspector2.types.covered_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.covered_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> CoveredResources:
    import aws_sdk_inspector2.types.covered_resource

    out: CoveredResources = []
    for item in data:
        out.append(aws_sdk_inspector2.types.covered_resource.deserialize_json(item))
    return out
