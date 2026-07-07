"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#CrlDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_rolesanywhere.types.uuid


class CrlDetail(TypedDict, closed=True):
    crl_id: NotRequired["aws_sdk_rolesanywhere.types.uuid.Uuid"]
    """<p>The unique identifier of the certificate revocation list (CRL).</p>"""
    crl_arn: NotRequired["str"]
    """<p>The ARN of the certificate revocation list (CRL).</p>"""
    name: NotRequired["str"]
    """<p>The name of the certificate revocation list (CRL).</p>"""
    enabled: NotRequired["bool"]
    """<p>Indicates whether the certificate revocation list (CRL) is enabled.</p>"""
    crl_data: NotRequired["bytes"]
    """<p>The state of the certificate revocation list (CRL) after a read or write operation.</p>"""
    trust_anchor_arn: NotRequired["str"]
    """<p>The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the certificate revocation list (CRL) was created. </p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 timestamp when the certificate revocation list (CRL) was last updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrlDetail) -> dict:
    out: dict = {}
    if "crl_id" in value:
        out["crlId"] = value["crl_id"]
    if "crl_arn" in value:
        out["crlArn"] = value["crl_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "crl_data" in value:
        import aws_sdk_rolesanywhere.types._prelude.blob

        out["crlData"] = aws_sdk_rolesanywhere.types._prelude.blob.serialize_json(
            value["crl_data"]
        )
    if "trust_anchor_arn" in value:
        out["trustAnchorArn"] = value["trust_anchor_arn"]
    if "created_at" in value:
        import aws_sdk_rolesanywhere.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_rolesanywhere.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_rolesanywhere.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_rolesanywhere.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> CrlDetail:
    out: CrlDetail = {}  # type: ignore[typeddict-item]
    if "crlId" in data:
        out["crl_id"] = data["crlId"]
    if "crlArn" in data:
        out["crl_arn"] = data["crlArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "crlData" in data:
        import aws_sdk_rolesanywhere.types._prelude.blob

        out["crl_data"] = aws_sdk_rolesanywhere.types._prelude.blob.deserialize_json(
            data["crlData"]
        )
    if "trustAnchorArn" in data:
        out["trust_anchor_arn"] = data["trustAnchorArn"]
    if "createdAt" in data:
        import aws_sdk_rolesanywhere.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_rolesanywhere.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_rolesanywhere.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_rolesanywhere.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
