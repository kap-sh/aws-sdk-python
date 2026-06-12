"""Generated from Smithy shape ``com.amazonaws.glue#GetDevEndpointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.dev_endpoint_list
    import aws_sdk_glue.types.generic_string


class GetDevEndpointsResponse(TypedDict):
    dev_endpoints: NotRequired["aws_sdk_glue.types.dev_endpoint_list.DevEndpointList"]
    """<p>A list of <code>DevEndpoint</code> definitions.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if not all <code>DevEndpoint</code> definitions have yet been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDevEndpointsResponse) -> dict:
    out: dict = {}
    if "dev_endpoints" in value:
        import aws_sdk_glue.types.dev_endpoint_list

        out["DevEndpoints"] = (
            aws_sdk_glue.types.dev_endpoint_list.serialize_aws_json_1_1(
                value["dev_endpoints"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDevEndpointsResponse:
    out: GetDevEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "DevEndpoints" in data:
        import aws_sdk_glue.types.dev_endpoint_list

        out["dev_endpoints"] = (
            aws_sdk_glue.types.dev_endpoint_list.deserialize_aws_json_1_1(
                data["DevEndpoints"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
