"""Generated from Smithy shape ``com.amazonaws.lakeformation#BatchPermissionsRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.batch_permissions_request_entry

BatchPermissionsRequestEntryList: TypeAlias = list[
    "capo_lakeformation.types.batch_permissions_request_entry.BatchPermissionsRequestEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPermissionsRequestEntryList) -> list:
    import capo_lakeformation.types.batch_permissions_request_entry

    out: list = []
    for item in value:
        out.append(
            capo_lakeformation.types.batch_permissions_request_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchPermissionsRequestEntryList:
    import capo_lakeformation.types.batch_permissions_request_entry

    out: BatchPermissionsRequestEntryList = []
    for item in data:
        out.append(
            capo_lakeformation.types.batch_permissions_request_entry.deserialize_json(
                item
            )
        )
    return out
