"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribePublisherInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.publisher_id


class DescribePublisherInput(TypedDict, closed=True):
    publisher_id: NotRequired["capo_cloudformation.types.publisher_id.PublisherId"]
    """<p>The ID of the extension publisher.</p> <p>If you don't supply a <code>PublisherId</code>, and you have registered as an extension publisher, <code>DescribePublisher</code> returns information about your own publisher account.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribePublisherInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "publisher_id" in value:
        pairs.append((f"{prefix}.PublisherId", str(value["publisher_id"])))


def deserialize_query(el: Element) -> DescribePublisherInput:
    out: DescribePublisherInput = {}  # type: ignore[typeddict-item]
    child_publisher_id = el.find("PublisherId")
    if child_publisher_id is not None:
        out["publisher_id"] = str(child_publisher_id.text or "")
    return out
