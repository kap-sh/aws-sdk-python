"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#Queue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.string


class Queue(TypedDict, closed=True):
    name: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The name of the queue.</p>"""
    url: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The URL of the queue.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Queue, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "url" in value:
        pairs.append((f"{key_prefix}URL", str(value["url"])))


def deserialize_query(el: Element) -> Queue:
    out: Queue = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_url = el.find("URL")
    if child_url is not None:
        out["url"] = str(child_url.text or "")
    return out
