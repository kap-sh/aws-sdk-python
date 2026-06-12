"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ErrorEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.batch_put_property_error_entry

ErrorEntries: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.batch_put_property_error_entry.BatchPutPropertyErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorEntries) -> list:
    import aws_sdk_iottwinmaker.types.batch_put_property_error_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iottwinmaker.types.batch_put_property_error_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ErrorEntries:
    import aws_sdk_iottwinmaker.types.batch_put_property_error_entry

    out: ErrorEntries = []
    for item in data:
        out.append(
            aws_sdk_iottwinmaker.types.batch_put_property_error_entry.deserialize_json(
                item
            )
        )
    return out
