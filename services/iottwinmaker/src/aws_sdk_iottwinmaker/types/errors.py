"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#Errors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.batch_put_property_error

Errors: TypeAlias = list[
    "aws_sdk_iottwinmaker.types.batch_put_property_error.BatchPutPropertyError"
]


# --- restJson1 ser/de ---
def serialize_json(value: Errors) -> list:
    import aws_sdk_iottwinmaker.types.batch_put_property_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iottwinmaker.types.batch_put_property_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> Errors:
    import aws_sdk_iottwinmaker.types.batch_put_property_error

    out: Errors = []
    for item in data:
        out.append(
            aws_sdk_iottwinmaker.types.batch_put_property_error.deserialize_json(item)
        )
    return out
