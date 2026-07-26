"""Generated from Smithy shape ``com.amazonaws.connect#HoursOfOperationOverrideConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation_override_config

HoursOfOperationOverrideConfigList: TypeAlias = list[
    "capo_connect.types.hours_of_operation_override_config.HoursOfOperationOverrideConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: HoursOfOperationOverrideConfigList) -> list:
    import capo_connect.types.hours_of_operation_override_config

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.hours_of_operation_override_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HoursOfOperationOverrideConfigList:
    import capo_connect.types.hours_of_operation_override_config

    out: HoursOfOperationOverrideConfigList = []
    for item in data:
        out.append(
            capo_connect.types.hours_of_operation_override_config.deserialize_json(item)
        )
    return out
