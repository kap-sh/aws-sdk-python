"""Generated from Smithy shape ``com.amazonaws.lakeformation#BatchPermissionsFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.batch_permissions_failure_entry

BatchPermissionsFailureList: TypeAlias = list[
    "aws_sdk_lakeformation.types.batch_permissions_failure_entry.BatchPermissionsFailureEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPermissionsFailureList) -> list:
    import aws_sdk_lakeformation.types.batch_permissions_failure_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lakeformation.types.batch_permissions_failure_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchPermissionsFailureList:
    import aws_sdk_lakeformation.types.batch_permissions_failure_entry

    out: BatchPermissionsFailureList = []
    for item in data:
        out.append(
            aws_sdk_lakeformation.types.batch_permissions_failure_entry.deserialize_json(
                item
            )
        )
    return out
