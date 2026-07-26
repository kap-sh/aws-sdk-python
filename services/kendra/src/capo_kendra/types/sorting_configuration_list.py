"""Generated from Smithy shape ``com.amazonaws.kendra#SortingConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.sorting_configuration

SortingConfigurationList: TypeAlias = list[
    "capo_kendra.types.sorting_configuration.SortingConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortingConfigurationList) -> list:
    import capo_kendra.types.sorting_configuration

    out: list = []
    for item in value:
        out.append(capo_kendra.types.sorting_configuration.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SortingConfigurationList:
    import capo_kendra.types.sorting_configuration

    out: SortingConfigurationList = []
    for item in data:
        out.append(
            capo_kendra.types.sorting_configuration.deserialize_aws_json_1_1(item)
        )
    return out
