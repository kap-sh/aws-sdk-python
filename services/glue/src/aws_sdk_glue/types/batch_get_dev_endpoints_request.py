"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetDevEndpointsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.dev_endpoint_names


class BatchGetDevEndpointsRequest(TypedDict):
    dev_endpoint_names: "aws_sdk_glue.types.dev_endpoint_names.DevEndpointNames"
    """<p>The list of <code>DevEndpoint</code> names, which might be the names returned from the <code>ListDevEndpoint</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDevEndpointsRequest) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.dev_endpoint_names

    out["DevEndpointNames"] = (
        aws_sdk_glue.types.dev_endpoint_names.serialize_aws_json_1_1(
            value["dev_endpoint_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDevEndpointsRequest:
    out: BatchGetDevEndpointsRequest = {}  # type: ignore[typeddict-item]
    if "DevEndpointNames" in data:
        import aws_sdk_glue.types.dev_endpoint_names

        out["dev_endpoint_names"] = (
            aws_sdk_glue.types.dev_endpoint_names.deserialize_aws_json_1_1(
                data["DevEndpointNames"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetDevEndpointsRequest.dev_endpoint_names required"
        )
    return out
