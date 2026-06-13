"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#CrlDetailResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.crl_detail


class CrlDetailResponse(TypedDict):
    crl: "aws_sdk_rolesanywhere.types.crl_detail.CrlDetail"
    """<p>The state of the certificate revocation list (CRL) after a read or write operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrlDetailResponse) -> dict:
    out: dict = {}
    import aws_sdk_rolesanywhere.types.crl_detail

    out["crl"] = aws_sdk_rolesanywhere.types.crl_detail.serialize_json(value["crl"])
    return out


def deserialize_json(data: dict) -> CrlDetailResponse:
    out: CrlDetailResponse = {}  # type: ignore[typeddict-item]
    if "crl" in data:
        import aws_sdk_rolesanywhere.types.crl_detail

        out["crl"] = aws_sdk_rolesanywhere.types.crl_detail.deserialize_json(
            data["crl"]
        )
    else:
        raise DeserializationError("CrlDetailResponse.crl required")
    return out
