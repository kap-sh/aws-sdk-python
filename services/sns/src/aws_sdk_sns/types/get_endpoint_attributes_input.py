"""Generated from Smithy shape ``com.amazonaws.sns#GetEndpointAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.string


class GetEndpointAttributesInput(TypedDict, closed=True):
    endpoint_arn: "aws_sdk_sns.types.string.String"
    """<p> <code>EndpointArn</code> for <code>GetEndpointAttributes</code> input.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetEndpointAttributesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.EndpointArn", str(value["endpoint_arn"])))


def deserialize_query(el: Element) -> GetEndpointAttributesInput:
    out: GetEndpointAttributesInput = {}  # type: ignore[typeddict-item]
    child_endpoint_arn = el.find("EndpointArn")
    if child_endpoint_arn is not None:
        out["endpoint_arn"] = str(child_endpoint_arn.text or "")
    else:
        raise DeserializationError("GetEndpointAttributesInput.endpoint_arn required")
    return out
