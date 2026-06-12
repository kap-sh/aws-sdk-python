"""Generated from Smithy shape ``com.amazonaws.pricing#GetProductsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pricing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pricing.types.filters
    import aws_sdk_pricing.types.format_version
    import aws_sdk_pricing.types.get_products_max_results
    import aws_sdk_pricing.types.string


class GetProductsRequest(TypedDict):
    service_code: "aws_sdk_pricing.types.string.String"
    """<p>The code for the service whose products you want to retrieve. </p>"""
    filters: NotRequired["aws_sdk_pricing.types.filters.Filters"]
    """<p>The list of filters that limit the returned products. only products that match all filters are returned.</p>"""
    format_version: NotRequired["aws_sdk_pricing.types.format_version.FormatVersion"]
    """<p>The format version that you want the response to be in.</p> <p>Valid values are: <code>aws_v1</code> </p>"""
    next_token: NotRequired["aws_sdk_pricing.types.string.String"]
    """<p>The pagination token that indicates the next set of results that you want to retrieve.</p>"""
    max_results: NotRequired[
        "aws_sdk_pricing.types.get_products_max_results.GetProductsMaxResults"
    ]
    """<p>The maximum number of results to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetProductsRequest) -> dict:
    out: dict = {}
    out["ServiceCode"] = value["service_code"]
    if "filters" in value:
        import aws_sdk_pricing.types.filters

        out["Filters"] = aws_sdk_pricing.types.filters.serialize_aws_json_1_1(
            value["filters"]
        )
    if "format_version" in value:
        out["FormatVersion"] = value["format_version"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetProductsRequest:
    out: GetProductsRequest = {}  # type: ignore[typeddict-item]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    else:
        raise DeserializationError("GetProductsRequest.service_code required")
    if "Filters" in data:
        import aws_sdk_pricing.types.filters

        out["filters"] = aws_sdk_pricing.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "FormatVersion" in data:
        out["format_version"] = data["FormatVersion"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
