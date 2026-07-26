"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DisassociateCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string


class DisassociateCertificateRequest(TypedDict, closed=True):
    arn: "capo_mediaconvert.types.__string.__string"
    """The ARN of the ACM certificate that you want to disassociate from your MediaConvert resource."""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateCertificateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateCertificateRequest:
    out: DisassociateCertificateRequest = {}  # type: ignore[typeddict-item]
    return out
