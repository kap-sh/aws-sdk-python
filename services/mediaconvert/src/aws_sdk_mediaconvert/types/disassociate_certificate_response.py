"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DisassociateCertificateResponse``."""

from typing_extensions import TypedDict


class DisassociateCertificateResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateCertificateResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateCertificateResponse:
    out: DisassociateCertificateResponse = {}  # type: ignore[typeddict-item]
    return out
