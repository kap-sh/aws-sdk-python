"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#LoadBalancer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.resource_id


class LoadBalancer(TypedDict, closed=True):
    name: NotRequired["capo_elastic_beanstalk.types.resource_id.ResourceId"]
    """<p>The name of the LoadBalancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LoadBalancer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))


def deserialize_query(el: Element) -> LoadBalancer:
    out: LoadBalancer = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
