"""Generated from Smithy shape ``com.amazonaws.sustainability#GetEstimatedCarbonEmissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sustainability.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sustainability.types.estimated_carbon_emissions_list
    import aws_sdk_sustainability.types.next_token


class GetEstimatedCarbonEmissionsResponse(TypedDict):
    results: "aws_sdk_sustainability.types.estimated_carbon_emissions_list.EstimatedCarbonEmissionsList"
    """<p>The result of the requested inputs.</p>"""
    next_token: NotRequired["aws_sdk_sustainability.types.next_token.NextToken"]
    """<p>The pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEstimatedCarbonEmissionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_sustainability.types.estimated_carbon_emissions_list

    out["Results"] = (
        aws_sdk_sustainability.types.estimated_carbon_emissions_list.serialize_json(
            value["results"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetEstimatedCarbonEmissionsResponse:
    out: GetEstimatedCarbonEmissionsResponse = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_sustainability.types.estimated_carbon_emissions_list

        out["results"] = (
            aws_sdk_sustainability.types.estimated_carbon_emissions_list.deserialize_json(
                data["Results"]
            )
        )
    else:
        raise DeserializationError(
            "GetEstimatedCarbonEmissionsResponse.results required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
