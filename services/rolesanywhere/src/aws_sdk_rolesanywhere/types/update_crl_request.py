"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#UpdateCrlRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.resource_name
    import aws_sdk_rolesanywhere.types.uuid


class UpdateCrlRequest(TypedDict):
    crl_id: "aws_sdk_rolesanywhere.types.uuid.Uuid"
    """<p>The unique identifier of the certificate revocation list (CRL).</p>"""
    name: NotRequired["aws_sdk_rolesanywhere.types.resource_name.ResourceName"]
    """<p>The name of the Crl.</p>"""
    crl_data: NotRequired["bytes"]
    """<p>The x509 v3 specified certificate revocation list (CRL).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCrlRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "crl_data" in value:
        import aws_sdk_rolesanywhere.types._prelude.blob

        out["crlData"] = aws_sdk_rolesanywhere.types._prelude.blob.serialize_json(
            value["crl_data"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCrlRequest:
    out: UpdateCrlRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "crlData" in data:
        import aws_sdk_rolesanywhere.types._prelude.blob

        out["crl_data"] = aws_sdk_rolesanywhere.types._prelude.blob.deserialize_json(
            data["crlData"]
        )
    return out
