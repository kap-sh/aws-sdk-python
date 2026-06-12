"""Generated from Smithy shape ``com.amazonaws.m2#ApplicationVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_m2.types.application_version_summary

ApplicationVersionSummaryList: TypeAlias = list[
    "aws_sdk_m2.types.application_version_summary.ApplicationVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationVersionSummaryList) -> list:
    import aws_sdk_m2.types.application_version_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_m2.types.application_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationVersionSummaryList:
    import aws_sdk_m2.types.application_version_summary

    out: ApplicationVersionSummaryList = []
    for item in data:
        out.append(aws_sdk_m2.types.application_version_summary.deserialize_json(item))
    return out
