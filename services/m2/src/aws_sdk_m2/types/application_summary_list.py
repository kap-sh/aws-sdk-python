"""Generated from Smithy shape ``com.amazonaws.m2#ApplicationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_m2.types.application_summary

ApplicationSummaryList: TypeAlias = list[
    "aws_sdk_m2.types.application_summary.ApplicationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummaryList) -> list:
    import aws_sdk_m2.types.application_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_m2.types.application_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationSummaryList:
    import aws_sdk_m2.types.application_summary

    out: ApplicationSummaryList = []
    for item in data:
        out.append(aws_sdk_m2.types.application_summary.deserialize_json(item))
    return out
