"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.finding_details

FindingDetailsList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.finding_details.FindingDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingDetailsList) -> list:
    import aws_sdk_accessanalyzer.types.finding_details

    out: list = []
    for item in value:
        out.append(aws_sdk_accessanalyzer.types.finding_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingDetailsList:
    import aws_sdk_accessanalyzer.types.finding_details

    out: FindingDetailsList = []
    for item in data:
        out.append(aws_sdk_accessanalyzer.types.finding_details.deserialize_json(item))
    return out
