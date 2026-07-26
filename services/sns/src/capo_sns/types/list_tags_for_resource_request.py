"""Generated from Smithy shape ``com.amazonaws.sns#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.amazon_resource_name


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_sns.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the topic for which to list tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTagsForResourceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))


def deserialize_query(el: Element) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    return out
