"""Generated from Smithy shape ``com.amazonaws.ecs#KeyValuePair``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class KeyValuePair(TypedDict, closed=True):
    name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the key-value pair. For environment variables, this is the name of the environment variable.</p>"""
    value: NotRequired["capo_ecs.types.string.String"]
    """<p>The value of the key-value pair. For environment variables, this is the value of the environment variable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyValuePair) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KeyValuePair:
    out: KeyValuePair = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
