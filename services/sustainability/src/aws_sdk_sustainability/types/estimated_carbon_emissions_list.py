"""Generated from Smithy shape ``com.amazonaws.sustainability#EstimatedCarbonEmissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sustainability.types.estimated_carbon_emissions

EstimatedCarbonEmissionsList: TypeAlias = list[
    "aws_sdk_sustainability.types.estimated_carbon_emissions.EstimatedCarbonEmissions"
]


# --- restJson1 ser/de ---
def serialize_json(value: EstimatedCarbonEmissionsList) -> list:
    import aws_sdk_sustainability.types.estimated_carbon_emissions

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sustainability.types.estimated_carbon_emissions.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EstimatedCarbonEmissionsList:
    import aws_sdk_sustainability.types.estimated_carbon_emissions

    out: EstimatedCarbonEmissionsList = []
    for item in data:
        out.append(
            aws_sdk_sustainability.types.estimated_carbon_emissions.deserialize_json(
                item
            )
        )
    return out
