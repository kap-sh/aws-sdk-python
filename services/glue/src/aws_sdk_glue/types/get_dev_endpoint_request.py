"""Generated from Smithy shape ``com.amazonaws.glue#GetDevEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string


class GetDevEndpointRequest(TypedDict):
    endpoint_name: "aws_sdk_glue.types.generic_string.GenericString"
    """<p>Name of the <code>DevEndpoint</code> to retrieve information for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDevEndpointRequest) -> dict:
    out: dict = {}
    out["EndpointName"] = value["endpoint_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDevEndpointRequest:
    out: GetDevEndpointRequest = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    else:
        raise DeserializationError("GetDevEndpointRequest.endpoint_name required")
    return out
