"""Generated from Smithy shape ``com.amazonaws.kafka#Iam``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__boolean


class Iam(TypedDict):
    enabled: NotRequired["aws_sdk_kafka.types.__boolean.__boolean"]
    """<p>Indicates whether IAM access control is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Iam) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> Iam:
    out: Iam = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
