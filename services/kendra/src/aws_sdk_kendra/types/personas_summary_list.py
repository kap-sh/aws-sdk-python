"""Generated from Smithy shape ``com.amazonaws.kendra#PersonasSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.personas_summary

PersonasSummaryList: TypeAlias = list[
    "aws_sdk_kendra.types.personas_summary.PersonasSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersonasSummaryList) -> list:
    import aws_sdk_kendra.types.personas_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.personas_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PersonasSummaryList:
    import aws_sdk_kendra.types.personas_summary

    out: PersonasSummaryList = []
    for item in data:
        out.append(aws_sdk_kendra.types.personas_summary.deserialize_aws_json_1_1(item))
    return out
