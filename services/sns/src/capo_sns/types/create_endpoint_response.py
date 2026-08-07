"""Generated from Smithy shape ``com.amazonaws.sns#CreateEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.string


class CreateEndpointResponse(TypedDict, closed=True):
    endpoint_arn: NotRequired["capo_sns.types.string.String"]
    """<p>EndpointArn returned from CreateEndpoint action.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateEndpointResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "endpoint_arn" in value:
        pairs.append((f"{key_prefix}EndpointArn", str(value["endpoint_arn"])))


def deserialize_query(el: Element) -> CreateEndpointResponse:
    out: CreateEndpointResponse = {}  # type: ignore[typeddict-item]
    child_endpoint_arn = el.find("EndpointArn")
    if child_endpoint_arn is not None:
        out["endpoint_arn"] = str(child_endpoint_arn.text or "")
    return out
