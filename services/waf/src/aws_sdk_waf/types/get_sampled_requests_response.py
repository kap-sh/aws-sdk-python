"""Generated from Smithy shape ``com.amazonaws.waf#GetSampledRequestsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf.types.population_size
    import aws_sdk_waf.types.sampled_http_requests
    import aws_sdk_waf.types.time_window


class GetSampledRequestsResponse(TypedDict, closed=True):
    sampled_requests: NotRequired[
        "aws_sdk_waf.types.sampled_http_requests.SampledHTTPRequests"
    ]
    """<p>A complex type that contains detailed information about each of the requests in the sample.</p>"""
    population_size: "aws_sdk_waf.types.population_size.PopulationSize"
    """<p>The total number of requests from which <code>GetSampledRequests</code> got a sample of <code>MaxItems</code> requests. If <code>PopulationSize</code> is less than <code>MaxItems</code>, the sample includes every request that your AWS resource received during the specified time range.</p>"""
    time_window: NotRequired["aws_sdk_waf.types.time_window.TimeWindow"]
    """<p>Usually, <code>TimeWindow</code> is the time range that you specified in the <code>GetSampledRequests</code> request. However, if your AWS resource received more than 5,000 requests during the time range that you specified in the request, <code>GetSampledRequests</code> returns the time range for the first 5,000 requests. Times are in Coordinated Universal Time (UTC) format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSampledRequestsResponse) -> dict:
    out: dict = {}
    if "sampled_requests" in value:
        import aws_sdk_waf.types.sampled_http_requests

        out["SampledRequests"] = (
            aws_sdk_waf.types.sampled_http_requests.serialize_aws_json_1_1(
                value["sampled_requests"]
            )
        )
    out["PopulationSize"] = value.get("population_size", 0)
    if "time_window" in value:
        import aws_sdk_waf.types.time_window

        out["TimeWindow"] = aws_sdk_waf.types.time_window.serialize_aws_json_1_1(
            value["time_window"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSampledRequestsResponse:
    out: GetSampledRequestsResponse = {}  # type: ignore[typeddict-item]
    if "SampledRequests" in data:
        import aws_sdk_waf.types.sampled_http_requests

        out["sampled_requests"] = (
            aws_sdk_waf.types.sampled_http_requests.deserialize_aws_json_1_1(
                data["SampledRequests"]
            )
        )
    if "PopulationSize" in data:
        out["population_size"] = data["PopulationSize"]
    else:
        out["population_size"] = 0
    if "TimeWindow" in data:
        import aws_sdk_waf.types.time_window

        out["time_window"] = aws_sdk_waf.types.time_window.deserialize_aws_json_1_1(
            data["TimeWindow"]
        )
    return out
