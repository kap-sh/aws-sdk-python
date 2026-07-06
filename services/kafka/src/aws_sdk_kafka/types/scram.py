"""Generated from Smithy shape ``com.amazonaws.kafka#Scram``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__boolean


class Scram(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_kafka.types.__boolean.__boolean"]
    """<p>SASL/SCRAM authentication is enabled or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Scram) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> Scram:
    out: Scram = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
