"""Generated from Smithy shape ``com.amazonaws.gamelift#FilterInstanceStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.filter_instance_status

FilterInstanceStatuses: TypeAlias = list[
    "capo_gamelift.types.filter_instance_status.FilterInstanceStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterInstanceStatuses) -> list:
    import capo_gamelift.types.filter_instance_status

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.filter_instance_status.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FilterInstanceStatuses:
    import capo_gamelift.types.filter_instance_status

    out: FilterInstanceStatuses = []
    for item in data:
        out.append(
            capo_gamelift.types.filter_instance_status.deserialize_aws_json_1_1(item)
        )
    return out
