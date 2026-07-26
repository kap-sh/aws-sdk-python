"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#Listener``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.integer
    import capo_elastic_beanstalk.types.string


class Listener(TypedDict, closed=True):
    protocol: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The protocol that is used by the Listener.</p>"""
    port: "capo_elastic_beanstalk.types.integer.Integer"
    """<p>The port that is used by the Listener.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Listener, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "protocol" in value:
        pairs.append((f"{prefix}.Protocol", str(value["protocol"])))
    pairs.append((f"{prefix}.Port", str(value.get("port", 0))))


def deserialize_query(el: Element) -> Listener:
    out: Listener = {}  # type: ignore[typeddict-item]
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    else:
        out["port"] = 0
    return out
