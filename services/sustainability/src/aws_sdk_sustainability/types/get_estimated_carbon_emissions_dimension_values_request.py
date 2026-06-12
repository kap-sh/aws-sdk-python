"""Generated from Smithy shape ``com.amazonaws.sustainability#GetEstimatedCarbonEmissionsDimensionValuesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sustainability.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sustainability.types.dimension_list
    import aws_sdk_sustainability.types.max_results
    import aws_sdk_sustainability.types.next_token
    import aws_sdk_sustainability.types.time_period


class GetEstimatedCarbonEmissionsDimensionValuesRequest(TypedDict):
    time_period: "aws_sdk_sustainability.types.time_period.TimePeriod"
    """<p>The date range for fetching the dimension values.</p>"""
    dimensions: "aws_sdk_sustainability.types.dimension_list.DimensionList"
    """<p>The dimensions available for grouping estimated carbon emissions.</p>"""
    max_results: "aws_sdk_sustainability.types.max_results.MaxResults"
    """<p>The maximum number of results to return in a single call. Default is 40.</p>"""
    next_token: NotRequired["aws_sdk_sustainability.types.next_token.NextToken"]
    """<p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEstimatedCarbonEmissionsDimensionValuesRequest) -> dict:
    out: dict = {}
    import aws_sdk_sustainability.types.time_period

    out["TimePeriod"] = aws_sdk_sustainability.types.time_period.serialize_json(
        value["time_period"]
    )
    import aws_sdk_sustainability.types.dimension_list

    out["Dimensions"] = aws_sdk_sustainability.types.dimension_list.serialize_json(
        value["dimensions"]
    )
    out["MaxResults"] = value.get("max_results", 1000)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetEstimatedCarbonEmissionsDimensionValuesRequest:
    out: GetEstimatedCarbonEmissionsDimensionValuesRequest = {}  # type: ignore[typeddict-item]
    if "TimePeriod" in data:
        import aws_sdk_sustainability.types.time_period

        out["time_period"] = aws_sdk_sustainability.types.time_period.deserialize_json(
            data["TimePeriod"]
        )
    else:
        raise DeserializationError(
            "GetEstimatedCarbonEmissionsDimensionValuesRequest.time_period required"
        )
    if "Dimensions" in data:
        import aws_sdk_sustainability.types.dimension_list

        out["dimensions"] = (
            aws_sdk_sustainability.types.dimension_list.deserialize_json(
                data["Dimensions"]
            )
        )
    else:
        raise DeserializationError(
            "GetEstimatedCarbonEmissionsDimensionValuesRequest.dimensions required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 1000
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
