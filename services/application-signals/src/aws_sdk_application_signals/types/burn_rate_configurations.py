"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BurnRateConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.burn_rate_configuration

BurnRateConfigurations: TypeAlias = list[
    "aws_sdk_application_signals.types.burn_rate_configuration.BurnRateConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: BurnRateConfigurations) -> list:
    import aws_sdk_application_signals.types.burn_rate_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_signals.types.burn_rate_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BurnRateConfigurations:
    import aws_sdk_application_signals.types.burn_rate_configuration

    out: BurnRateConfigurations = []
    for item in data:
        out.append(
            aws_sdk_application_signals.types.burn_rate_configuration.deserialize_json(
                item
            )
        )
    return out
