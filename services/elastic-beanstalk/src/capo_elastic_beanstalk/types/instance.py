"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#Instance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.resource_id


class Instance(TypedDict, closed=True):
    id: NotRequired["capo_elastic_beanstalk.types.resource_id.ResourceId"]
    """<p>The ID of the Amazon EC2 instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Instance, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "id" in value:
        pairs.append((f"{prefix}.Id", str(value["id"])))


def deserialize_query(el: Element) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    return out
