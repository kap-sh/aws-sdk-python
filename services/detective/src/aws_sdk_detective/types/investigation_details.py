"""Generated from Smithy shape ``com.amazonaws.detective#InvestigationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_detective.types.investigation_detail

InvestigationDetails: TypeAlias = list[
    "aws_sdk_detective.types.investigation_detail.InvestigationDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationDetails) -> list:
    import aws_sdk_detective.types.investigation_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_detective.types.investigation_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> InvestigationDetails:
    import aws_sdk_detective.types.investigation_detail

    out: InvestigationDetails = []
    for item in data:
        out.append(aws_sdk_detective.types.investigation_detail.deserialize_json(item))
    return out
