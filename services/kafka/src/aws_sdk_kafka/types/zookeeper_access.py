"""Generated from Smithy shape ``com.amazonaws.kafka#ZookeeperAccess``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__boolean


class ZookeeperAccess(TypedDict):
    enabled: NotRequired["aws_sdk_kafka.types.__boolean.__boolean"]
    """<p>Zookeeper Access was on or off for the cluster</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ZookeeperAccess) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> ZookeeperAccess:
    out: ZookeeperAccess = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
