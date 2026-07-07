"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetDevEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.dev_endpoint_list
    import aws_sdk_glue.types.dev_endpoint_names


class BatchGetDevEndpointsResponse(TypedDict, closed=True):
    dev_endpoints: NotRequired["aws_sdk_glue.types.dev_endpoint_list.DevEndpointList"]
    """<p>A list of <code>DevEndpoint</code> definitions.</p>"""
    dev_endpoints_not_found: NotRequired[
        "aws_sdk_glue.types.dev_endpoint_names.DevEndpointNames"
    ]
    """<p>A list of <code>DevEndpoints</code> not found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDevEndpointsResponse) -> dict:
    out: dict = {}
    if "dev_endpoints" in value:
        import aws_sdk_glue.types.dev_endpoint_list

        out["DevEndpoints"] = (
            aws_sdk_glue.types.dev_endpoint_list.serialize_aws_json_1_1(
                value["dev_endpoints"]
            )
        )
    if "dev_endpoints_not_found" in value:
        import aws_sdk_glue.types.dev_endpoint_names

        out["DevEndpointsNotFound"] = (
            aws_sdk_glue.types.dev_endpoint_names.serialize_aws_json_1_1(
                value["dev_endpoints_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDevEndpointsResponse:
    out: BatchGetDevEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "DevEndpoints" in data:
        import aws_sdk_glue.types.dev_endpoint_list

        out["dev_endpoints"] = (
            aws_sdk_glue.types.dev_endpoint_list.deserialize_aws_json_1_1(
                data["DevEndpoints"]
            )
        )
    if "DevEndpointsNotFound" in data:
        import aws_sdk_glue.types.dev_endpoint_names

        out["dev_endpoints_not_found"] = (
            aws_sdk_glue.types.dev_endpoint_names.deserialize_aws_json_1_1(
                data["DevEndpointsNotFound"]
            )
        )
    return out
