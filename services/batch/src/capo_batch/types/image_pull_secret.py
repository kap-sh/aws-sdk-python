"""Generated from Smithy shape ``com.amazonaws.batch#ImagePullSecret``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class ImagePullSecret(TypedDict, closed=True):
    name: NotRequired["capo_batch.types.string.String"]
    """<p>Provides a unique identifier for the <code>ImagePullSecret</code>. This object is required when <code>EksPodProperties$imagePullSecrets</code> is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImagePullSecret) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ImagePullSecret:
    out: ImagePullSecret = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
