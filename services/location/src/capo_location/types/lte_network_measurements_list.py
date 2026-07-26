"""Generated from Smithy shape ``com.amazonaws.location#LteNetworkMeasurementsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.lte_network_measurements

LteNetworkMeasurementsList: TypeAlias = list[
    "capo_location.types.lte_network_measurements.LteNetworkMeasurements"
]


# --- restJson1 ser/de ---
def serialize_json(value: LteNetworkMeasurementsList) -> list:
    import capo_location.types.lte_network_measurements

    out: list = []
    for item in value:
        out.append(capo_location.types.lte_network_measurements.serialize_json(item))
    return out


def deserialize_json(data: list) -> LteNetworkMeasurementsList:
    import capo_location.types.lte_network_measurements

    out: LteNetworkMeasurementsList = []
    for item in data:
        out.append(capo_location.types.lte_network_measurements.deserialize_json(item))
    return out
