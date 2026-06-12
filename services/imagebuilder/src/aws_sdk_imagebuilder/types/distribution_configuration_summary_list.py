"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DistributionConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.distribution_configuration_summary

DistributionConfigurationSummaryList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.distribution_configuration_summary.DistributionConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DistributionConfigurationSummaryList) -> list:
    import aws_sdk_imagebuilder.types.distribution_configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.distribution_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DistributionConfigurationSummaryList:
    import aws_sdk_imagebuilder.types.distribution_configuration_summary

    out: DistributionConfigurationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.distribution_configuration_summary.deserialize_json(
                item
            )
        )
    return out
