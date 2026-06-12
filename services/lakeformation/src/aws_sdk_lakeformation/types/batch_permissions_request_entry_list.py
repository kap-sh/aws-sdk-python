"""Generated from Smithy shape ``com.amazonaws.lakeformation#BatchPermissionsRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.batch_permissions_request_entry

BatchPermissionsRequestEntryList: TypeAlias = list[
    "aws_sdk_lakeformation.types.batch_permissions_request_entry.BatchPermissionsRequestEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPermissionsRequestEntryList) -> list:
    import aws_sdk_lakeformation.types.batch_permissions_request_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lakeformation.types.batch_permissions_request_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchPermissionsRequestEntryList:
    import aws_sdk_lakeformation.types.batch_permissions_request_entry

    out: BatchPermissionsRequestEntryList = []
    for item in data:
        out.append(
            aws_sdk_lakeformation.types.batch_permissions_request_entry.deserialize_json(
                item
            )
        )
    return out
