"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#DocumentServiceWarning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.string


class DocumentServiceWarning(TypedDict, closed=True):
    message: NotRequired["capo_cloudsearch_domain.types.string.String"]
    """<p>The description for a warning returned by the document service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentServiceWarning) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DocumentServiceWarning:
    out: DocumentServiceWarning = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out
