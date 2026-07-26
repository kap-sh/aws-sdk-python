"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BurnRateConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.burn_rate_configuration

BurnRateConfigurations: TypeAlias = list[
    "capo_application_signals.types.burn_rate_configuration.BurnRateConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: BurnRateConfigurations) -> list:
    import capo_application_signals.types.burn_rate_configuration

    out: list = []
    for item in value:
        out.append(
            capo_application_signals.types.burn_rate_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BurnRateConfigurations:
    import capo_application_signals.types.burn_rate_configuration

    out: BurnRateConfigurations = []
    for item in data:
        out.append(
            capo_application_signals.types.burn_rate_configuration.deserialize_json(
                item
            )
        )
    return out
