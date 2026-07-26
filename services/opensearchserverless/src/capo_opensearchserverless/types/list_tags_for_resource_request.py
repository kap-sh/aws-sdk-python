"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchserverless.types.arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_opensearchserverless.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource. The resource must be active (not in the <code>DELETING</code> state), and must be owned by the account ID included in the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    return out
