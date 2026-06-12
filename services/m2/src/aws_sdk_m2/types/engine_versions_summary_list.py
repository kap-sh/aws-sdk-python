"""Generated from Smithy shape ``com.amazonaws.m2#EngineVersionsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_m2.types.engine_versions_summary

EngineVersionsSummaryList: TypeAlias = list[
    "aws_sdk_m2.types.engine_versions_summary.EngineVersionsSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EngineVersionsSummaryList) -> list:
    import aws_sdk_m2.types.engine_versions_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_m2.types.engine_versions_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EngineVersionsSummaryList:
    import aws_sdk_m2.types.engine_versions_summary

    out: EngineVersionsSummaryList = []
    for item in data:
        out.append(aws_sdk_m2.types.engine_versions_summary.deserialize_json(item))
    return out
