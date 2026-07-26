"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#DeletePresetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.id


class DeletePresetRequest(TypedDict, closed=True):
    id: "capo_elastic_transcoder.types.id.Id"
    """<p>The identifier of the preset for which you want to get detailed information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePresetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePresetRequest:
    out: DeletePresetRequest = {}  # type: ignore[typeddict-item]
    return out
