"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerLogRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_name
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.string


class GetContainerLogRequest(TypedDict):
    service_name: "aws_sdk_lightsail.types.container_service_name.ContainerServiceName"
    """<p>The name of the container service for which to get a container log.</p>"""
    container_name: "aws_sdk_lightsail.types.string.string"
    """<p>The name of the container that is either running or previously ran on the container service for which to return a log.</p>"""
    start_time: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The start of the time interval for which to get log data.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, specify <code>1538424000</code> as the start time.</p> </li> </ul> <p>You can convert a human-friendly time to Unix time format using a converter like <a href=\"https://www.epochconverter.com/\">Epoch converter</a>.</p>"""
    end_time: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The end of the time interval for which to get log data.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use an end time of October 1, 2018, at 9 PM UTC, specify <code>1538427600</code> as the end time.</p> </li> </ul> <p>You can convert a human-friendly time to Unix time format using a converter like <a href=\"https://www.epochconverter.com/\">Epoch converter</a>.</p>"""
    filter_pattern: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The pattern to use to filter the returned log events to a specific term.</p> <p>The following are a few examples of filter patterns that you can specify:</p> <ul> <li> <p>To return all log events, specify a filter pattern of <code>\"\"</code>.</p> </li> <li> <p>To exclude log events that contain the <code>ERROR</code> term, and return all other log events, specify a filter pattern of <code>\"-ERROR\"</code>.</p> </li> <li> <p>To return log events that contain the <code>ERROR</code> term, specify a filter pattern of <code>\"ERROR\"</code>.</p> </li> <li> <p>To return log events that contain both the <code>ERROR</code> and <code>Exception</code> terms, specify a filter pattern of <code>\"ERROR Exception\"</code>.</p> </li> <li> <p>To return log events that contain the <code>ERROR</code> <i>or</i> the <code>Exception</code> term, specify a filter pattern of <code>\"?ERROR ?Exception\"</code>.</p> </li> </ul>"""
    page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetContainerLog</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerLogRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerLogRequest:
    out: GetContainerLogRequest = {}  # type: ignore[typeddict-item]
    return out
