"""Generated from Smithy shape ``com.amazonaws.glue#GetDevEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.dev_endpoint


class GetDevEndpointResponse(TypedDict, closed=True):
    dev_endpoint: NotRequired["capo_glue.types.dev_endpoint.DevEndpoint"]
    """<p>A <code>DevEndpoint</code> definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDevEndpointResponse) -> dict:
    out: dict = {}
    if "dev_endpoint" in value:
        import capo_glue.types.dev_endpoint

        out["DevEndpoint"] = capo_glue.types.dev_endpoint.serialize_aws_json_1_1(
            value["dev_endpoint"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDevEndpointResponse:
    out: GetDevEndpointResponse = {}  # type: ignore[typeddict-item]
    if "DevEndpoint" in data:
        import capo_glue.types.dev_endpoint

        out["dev_endpoint"] = capo_glue.types.dev_endpoint.deserialize_aws_json_1_1(
            data["DevEndpoint"]
        )
    return out
