"""Generated from Smithy shape ``com.amazonaws.appconfig#ValidatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.validator

ValidatorList: TypeAlias = list["aws_sdk_appconfig.types.validator.Validator"]


# --- restJson1 ser/de ---
def serialize_json(value: ValidatorList) -> list:
    import aws_sdk_appconfig.types.validator

    out: list = []
    for item in value:
        out.append(aws_sdk_appconfig.types.validator.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValidatorList:
    import aws_sdk_appconfig.types.validator

    out: ValidatorList = []
    for item in data:
        out.append(aws_sdk_appconfig.types.validator.deserialize_json(item))
    return out
