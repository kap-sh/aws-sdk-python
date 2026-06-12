"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemTemplateFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.system_template_filter

SystemTemplateFilters: TypeAlias = list[
    "aws_sdk_iotthingsgraph.types.system_template_filter.SystemTemplateFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemTemplateFilters) -> list:
    import aws_sdk_iotthingsgraph.types.system_template_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotthingsgraph.types.system_template_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SystemTemplateFilters:
    import aws_sdk_iotthingsgraph.types.system_template_filter

    out: SystemTemplateFilters = []
    for item in data:
        out.append(
            aws_sdk_iotthingsgraph.types.system_template_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
