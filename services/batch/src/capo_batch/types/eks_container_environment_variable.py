"""Generated from Smithy shape ``com.amazonaws.batch#EksContainerEnvironmentVariable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class EksContainerEnvironmentVariable(TypedDict, closed=True):
    name: NotRequired["capo_batch.types.string.String"]
    """<p>The name of the environment variable.</p>"""
    value: NotRequired["capo_batch.types.string.String"]
    """<p>The value of the environment variable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksContainerEnvironmentVariable) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> EksContainerEnvironmentVariable:
    out: EksContainerEnvironmentVariable = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    return out
