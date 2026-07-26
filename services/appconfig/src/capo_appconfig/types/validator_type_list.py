"""Generated from Smithy shape ``com.amazonaws.appconfig#ValidatorTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.validator_type

ValidatorTypeList: TypeAlias = list["capo_appconfig.types.validator_type.ValidatorType"]


# --- restJson1 ser/de ---
def serialize_json(value: ValidatorTypeList) -> list:
    import capo_appconfig.types.validator_type

    out: list = []
    for item in value:
        out.append(capo_appconfig.types.validator_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValidatorTypeList:
    import capo_appconfig.types.validator_type

    out: ValidatorTypeList = []
    for item in data:
        out.append(capo_appconfig.types.validator_type.deserialize_json(item))
    return out
