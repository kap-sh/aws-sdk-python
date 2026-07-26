"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ResourceTypeStatisticsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.resource_type
    import capo_accessanalyzer.types.resource_type_details

ResourceTypeStatisticsMap: TypeAlias = dict[
    "capo_accessanalyzer.types.resource_type.ResourceType",
    "capo_accessanalyzer.types.resource_type_details.ResourceTypeDetails",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ResourceTypeStatisticsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_accessanalyzer.types.resource_type_details

        out[key] = capo_accessanalyzer.types.resource_type_details.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ResourceTypeStatisticsMap:
    out: ResourceTypeStatisticsMap = {}
    for key, value in data.items():
        import capo_accessanalyzer.types.resource_type_details

        out[key] = capo_accessanalyzer.types.resource_type_details.deserialize_json(
            value
        )
    return out
