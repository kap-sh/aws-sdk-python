"""Generated from Smithy shape ``com.amazonaws.glue#GetDevEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.dev_endpoint_list
    import capo_glue.types.generic_string


class GetDevEndpointsResponse(TypedDict, closed=True):
    dev_endpoints: NotRequired["capo_glue.types.dev_endpoint_list.DevEndpointList"]
    """<p>A list of <code>DevEndpoint</code> definitions.</p>"""
    next_token: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if not all <code>DevEndpoint</code> definitions have yet been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDevEndpointsResponse) -> dict:
    out: dict = {}
    if "dev_endpoints" in value:
        import capo_glue.types.dev_endpoint_list

        out["DevEndpoints"] = capo_glue.types.dev_endpoint_list.serialize_aws_json_1_1(
            value["dev_endpoints"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDevEndpointsResponse:
    out: GetDevEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "DevEndpoints" in data:
        import capo_glue.types.dev_endpoint_list

        out["dev_endpoints"] = (
            capo_glue.types.dev_endpoint_list.deserialize_aws_json_1_1(
                data["DevEndpoints"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
