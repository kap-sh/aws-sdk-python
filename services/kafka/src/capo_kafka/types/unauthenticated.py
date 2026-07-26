"""Generated from Smithy shape ``com.amazonaws.kafka#Unauthenticated``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__boolean


class Unauthenticated(TypedDict, closed=True):
    enabled: NotRequired["capo_kafka.types.__boolean.__boolean"]
    """<p>Specifies whether you want to turn on or turn off unauthenticated traffic to your cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Unauthenticated) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> Unauthenticated:
    out: Unauthenticated = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
