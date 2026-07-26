"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemInstanceFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.system_instance_filter

SystemInstanceFilters: TypeAlias = list[
    "capo_iotthingsgraph.types.system_instance_filter.SystemInstanceFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemInstanceFilters) -> list:
    import capo_iotthingsgraph.types.system_instance_filter

    out: list = []
    for item in value:
        out.append(
            capo_iotthingsgraph.types.system_instance_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SystemInstanceFilters:
    import capo_iotthingsgraph.types.system_instance_filter

    out: SystemInstanceFilters = []
    for item in data:
        out.append(
            capo_iotthingsgraph.types.system_instance_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
