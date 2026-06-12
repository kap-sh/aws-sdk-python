"""Generated from Smithy shape ``com.amazonaws.appconfig#ValidatorTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.validator_type

ValidatorTypeList: TypeAlias = list[
    "aws_sdk_appconfig.types.validator_type.ValidatorType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidatorTypeList) -> list:
    import aws_sdk_appconfig.types.validator_type

    out: list = []
    for item in value:
        out.append(aws_sdk_appconfig.types.validator_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValidatorTypeList:
    import aws_sdk_appconfig.types.validator_type

    out: ValidatorTypeList = []
    for item in data:
        out.append(aws_sdk_appconfig.types.validator_type.deserialize_json(item))
    return out
