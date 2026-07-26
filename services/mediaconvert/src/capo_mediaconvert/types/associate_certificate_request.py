"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AssociateCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string


class AssociateCertificateRequest(TypedDict, closed=True):
    arn: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The ARN of the ACM certificate that you want to associate with your MediaConvert resource."""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateCertificateRequest) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> AssociateCertificateRequest:
    out: AssociateCertificateRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
