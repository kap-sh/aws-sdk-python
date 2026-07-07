"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#Limit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.max
    import aws_sdk_elastic_load_balancing.types.name


class Limit(TypedDict, closed=True):
    name: NotRequired["aws_sdk_elastic_load_balancing.types.name.Name"]
    """<p>The name of the limit. The possible values are:</p> <ul> <li> <p>classic-listeners</p> </li> <li> <p>classic-load-balancers</p> </li> <li> <p>classic-registered-instances</p> </li> </ul>"""
    max: NotRequired["aws_sdk_elastic_load_balancing.types.max.Max"]
    """<p>The maximum value of the limit.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Limit, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "max" in value:
        pairs.append((f"{prefix}.Max", str(value["max"])))


def deserialize_query(el: Element) -> Limit:
    out: Limit = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_max = el.find("Max")
    if child_max is not None:
        out["max"] = str(child_max.text or "")
    return out
