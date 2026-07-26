"""Generated from Smithy shape ``com.amazonaws.kendra#IndexConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.index_configuration_summary

IndexConfigurationSummaryList: TypeAlias = list[
    "capo_kendra.types.index_configuration_summary.IndexConfigurationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexConfigurationSummaryList) -> list:
    import capo_kendra.types.index_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.index_configuration_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IndexConfigurationSummaryList:
    import capo_kendra.types.index_configuration_summary

    out: IndexConfigurationSummaryList = []
    for item in data:
        out.append(
            capo_kendra.types.index_configuration_summary.deserialize_aws_json_1_1(item)
        )
    return out
