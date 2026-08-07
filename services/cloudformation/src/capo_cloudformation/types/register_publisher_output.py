"""Generated from Smithy shape ``com.amazonaws.cloudformation#RegisterPublisherOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.publisher_id


class RegisterPublisherOutput(TypedDict, closed=True):
    publisher_id: NotRequired["capo_cloudformation.types.publisher_id.PublisherId"]
    """<p>The ID assigned this account by CloudFormation for publishing extensions.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RegisterPublisherOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "publisher_id" in value:
        pairs.append((f"{key_prefix}PublisherId", str(value["publisher_id"])))


def deserialize_query(el: Element) -> RegisterPublisherOutput:
    out: RegisterPublisherOutput = {}  # type: ignore[typeddict-item]
    child_publisher_id = el.find("PublisherId")
    if child_publisher_id is not None:
        out["publisher_id"] = str(child_publisher_id.text or "")
    return out
