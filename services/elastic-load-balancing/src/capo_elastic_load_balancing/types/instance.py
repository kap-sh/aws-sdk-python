"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#Instance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.instance_id


class Instance(TypedDict, closed=True):
    instance_id: NotRequired["capo_elastic_load_balancing.types.instance_id.InstanceId"]
    """<p>The instance ID.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Instance, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))


def deserialize_query(el: Element) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    return out
