"""Generated from Smithy shape ``com.amazonaws.directoryservice#HybridUpdateInfoEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.hybrid_update_info_entry

HybridUpdateInfoEntries: TypeAlias = list[
    "capo_directory_service.types.hybrid_update_info_entry.HybridUpdateInfoEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HybridUpdateInfoEntries) -> list:
    import capo_directory_service.types.hybrid_update_info_entry

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.hybrid_update_info_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HybridUpdateInfoEntries:
    import capo_directory_service.types.hybrid_update_info_entry

    out: HybridUpdateInfoEntries = []
    for item in data:
        out.append(
            capo_directory_service.types.hybrid_update_info_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
