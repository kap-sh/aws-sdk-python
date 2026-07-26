"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.enabled_baseline_parameter

EnabledBaselineParameters: TypeAlias = list[
    "capo_controltower.types.enabled_baseline_parameter.EnabledBaselineParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineParameters) -> list:
    import capo_controltower.types.enabled_baseline_parameter

    out: list = []
    for item in value:
        out.append(
            capo_controltower.types.enabled_baseline_parameter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EnabledBaselineParameters:
    import capo_controltower.types.enabled_baseline_parameter

    out: EnabledBaselineParameters = []
    for item in data:
        out.append(
            capo_controltower.types.enabled_baseline_parameter.deserialize_json(item)
        )
    return out
