"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#ConnectionSettings``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element
from aws_sdk_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.idle_timeout


class ConnectionSettings(TypedDict):
    idle_timeout: "aws_sdk_elastic_load_balancing.types.idle_timeout.IdleTimeout"
    """<p>The time, in seconds, that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConnectionSettings, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.IdleTimeout", str(value["idle_timeout"])))


def deserialize_query(el: Element) -> ConnectionSettings:
    out: ConnectionSettings = {}  # type: ignore[typeddict-item]
    child_idle_timeout = el.find("IdleTimeout")
    if child_idle_timeout is not None:
        out["idle_timeout"] = int(child_idle_timeout.text or "")
    else:
        raise DeserializationError("ConnectionSettings.idle_timeout required")
    return out
