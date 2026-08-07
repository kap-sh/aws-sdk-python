"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#Trigger``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.resource_id


class Trigger(TypedDict, closed=True):
    name: NotRequired["capo_elastic_beanstalk.types.resource_id.ResourceId"]
    """<p>The name of the trigger.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Trigger, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))


def deserialize_query(el: Element) -> Trigger:
    out: Trigger = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
