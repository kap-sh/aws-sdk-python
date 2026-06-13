"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ScalarCrlRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.uuid


class ScalarCrlRequest(TypedDict):
    crl_id: "aws_sdk_rolesanywhere.types.uuid.Uuid"
    """<p>The unique identifier of the certificate revocation list (CRL).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScalarCrlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ScalarCrlRequest:
    out: ScalarCrlRequest = {}  # type: ignore[typeddict-item]
    return out
