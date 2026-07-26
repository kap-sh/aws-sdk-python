"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Warning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.string


class Warning(TypedDict, closed=True):
    code: NotRequired["capo_elastic_transcoder.types.string.String"]
    """<p>The code of the cross-regional warning.</p>"""
    message: NotRequired["capo_elastic_transcoder.types.string.String"]
    """<p>The message explaining what resources are in a different region from the pipeline.</p> <note> <p>AWS KMS keys must be in the same region as the pipeline.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: Warning) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> Warning:
    out: Warning = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
