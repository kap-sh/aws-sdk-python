"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateActivities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.update_info_entry

UpdateActivities: TypeAlias = list[
    "capo_directory_service.types.update_info_entry.UpdateInfoEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateActivities) -> list:
    import capo_directory_service.types.update_info_entry

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.update_info_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UpdateActivities:
    import capo_directory_service.types.update_info_entry

    out: UpdateActivities = []
    for item in data:
        out.append(
            capo_directory_service.types.update_info_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
