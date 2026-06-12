"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#Queue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.string


class Queue(TypedDict):
    name: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>The name of the queue.</p>"""
    url: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>The URL of the queue.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Queue, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "url" in value:
        pairs.append((f"{prefix}.URL", str(value["url"])))


def deserialize_query(el: Element) -> Queue:
    out: Queue = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_url = el.find("URL")
    if child_url is not None:
        out["url"] = str(child_url.text or "")
    return out
