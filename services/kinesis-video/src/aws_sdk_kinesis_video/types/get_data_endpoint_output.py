"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#GetDataEndpointOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.data_endpoint


class GetDataEndpointOutput(TypedDict, closed=True):
    data_endpoint: NotRequired["aws_sdk_kinesis_video.types.data_endpoint.DataEndpoint"]
    """<p>The endpoint value. To read data from the stream or to write data to it, specify this endpoint in your application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataEndpointOutput) -> dict:
    out: dict = {}
    if "data_endpoint" in value:
        out["DataEndpoint"] = value["data_endpoint"]
    return out


def deserialize_json(data: dict) -> GetDataEndpointOutput:
    out: GetDataEndpointOutput = {}  # type: ignore[typeddict-item]
    if "DataEndpoint" in data:
        out["data_endpoint"] = data["DataEndpoint"]
    return out
