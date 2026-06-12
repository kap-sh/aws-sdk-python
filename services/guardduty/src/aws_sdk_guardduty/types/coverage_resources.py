"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.coverage_resource

CoverageResources: TypeAlias = list[
    "aws_sdk_guardduty.types.coverage_resource.CoverageResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoverageResources) -> list:
    import aws_sdk_guardduty.types.coverage_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.coverage_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> CoverageResources:
    import aws_sdk_guardduty.types.coverage_resource

    out: CoverageResources = []
    for item in data:
        out.append(aws_sdk_guardduty.types.coverage_resource.deserialize_json(item))
    return out
