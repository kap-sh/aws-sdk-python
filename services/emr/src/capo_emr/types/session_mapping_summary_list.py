"""Generated from Smithy shape ``com.amazonaws.emr#SessionMappingSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.session_mapping_summary

SessionMappingSummaryList: TypeAlias = list[
    "capo_emr.types.session_mapping_summary.SessionMappingSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionMappingSummaryList) -> list:
    import capo_emr.types.session_mapping_summary

    out: list = []
    for item in value:
        out.append(capo_emr.types.session_mapping_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SessionMappingSummaryList:
    import capo_emr.types.session_mapping_summary

    out: SessionMappingSummaryList = []
    for item in data:
        out.append(
            capo_emr.types.session_mapping_summary.deserialize_aws_json_1_1(item)
        )
    return out
