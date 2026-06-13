"""Generated from Smithy shape ``com.amazonaws.freetier#FilterActivityStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_freetier.types.activity_status

FilterActivityStatuses: TypeAlias = list[
    "aws_sdk_freetier.types.activity_status.ActivityStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FilterActivityStatuses) -> list:
    import aws_sdk_freetier.types.activity_status

    out: list = []
    for item in value:
        out.append(aws_sdk_freetier.types.activity_status.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> FilterActivityStatuses:
    import aws_sdk_freetier.types.activity_status

    out: FilterActivityStatuses = []
    for item in data:
        out.append(
            aws_sdk_freetier.types.activity_status.deserialize_aws_json_1_0(item)
        )
    return out
