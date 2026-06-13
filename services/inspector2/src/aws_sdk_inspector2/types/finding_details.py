"""Generated from Smithy shape ``com.amazonaws.inspector2#FindingDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.finding_detail

FindingDetails: TypeAlias = list[
    "aws_sdk_inspector2.types.finding_detail.FindingDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingDetails) -> list:
    import aws_sdk_inspector2.types.finding_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.finding_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingDetails:
    import aws_sdk_inspector2.types.finding_detail

    out: FindingDetails = []
    for item in data:
        out.append(aws_sdk_inspector2.types.finding_detail.deserialize_json(item))
    return out
