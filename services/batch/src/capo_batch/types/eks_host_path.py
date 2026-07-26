"""Generated from Smithy shape ``com.amazonaws.batch#EksHostPath``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class EksHostPath(TypedDict, closed=True):
    path: NotRequired["capo_batch.types.string.String"]
    """<p>The path of the file or directory on the host to mount into containers on the pod.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksHostPath) -> dict:
    out: dict = {}
    if "path" in value:
        out["path"] = value["path"]
    return out


def deserialize_json(data: dict) -> EksHostPath:
    out: EksHostPath = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    return out
