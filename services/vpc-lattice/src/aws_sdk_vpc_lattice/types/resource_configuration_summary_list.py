"""Generated from Smithy shape ``com.amazonaws.vpclattice#ResourceConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.resource_configuration_summary

ResourceConfigurationSummaryList: TypeAlias = list[
    "aws_sdk_vpc_lattice.types.resource_configuration_summary.ResourceConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceConfigurationSummaryList) -> list:
    import aws_sdk_vpc_lattice.types.resource_configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_vpc_lattice.types.resource_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResourceConfigurationSummaryList:
    import aws_sdk_vpc_lattice.types.resource_configuration_summary

    out: ResourceConfigurationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_vpc_lattice.types.resource_configuration_summary.deserialize_json(
                item
            )
        )
    return out
