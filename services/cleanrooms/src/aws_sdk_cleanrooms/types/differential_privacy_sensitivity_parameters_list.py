"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacySensitivityParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.differential_privacy_sensitivity_parameters

DifferentialPrivacySensitivityParametersList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.differential_privacy_sensitivity_parameters.DifferentialPrivacySensitivityParameters"
]


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacySensitivityParametersList) -> list:
    import aws_sdk_cleanrooms.types.differential_privacy_sensitivity_parameters

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.differential_privacy_sensitivity_parameters.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DifferentialPrivacySensitivityParametersList:
    import aws_sdk_cleanrooms.types.differential_privacy_sensitivity_parameters

    out: DifferentialPrivacySensitivityParametersList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.differential_privacy_sensitivity_parameters.deserialize_json(
                item
            )
        )
    return out
