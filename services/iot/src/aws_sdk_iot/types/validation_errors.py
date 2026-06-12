"""Generated from Smithy shape ``com.amazonaws.iot#ValidationErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.validation_error

ValidationErrors: TypeAlias = list["aws_sdk_iot.types.validation_error.ValidationError"]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationErrors) -> list:
    import aws_sdk_iot.types.validation_error

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.validation_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValidationErrors:
    import aws_sdk_iot.types.validation_error

    out: ValidationErrors = []
    for item in data:
        out.append(aws_sdk_iot.types.validation_error.deserialize_json(item))
    return out
