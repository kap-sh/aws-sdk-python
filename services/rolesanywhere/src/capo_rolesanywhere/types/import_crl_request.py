"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ImportCrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rolesanywhere.types.resource_name
    import capo_rolesanywhere.types.tag_list
    import capo_rolesanywhere.types.trust_anchor_arn


class ImportCrlRequest(TypedDict, closed=True):
    name: "capo_rolesanywhere.types.resource_name.ResourceName"
    """<p>The name of the certificate revocation list (CRL).</p>"""
    crl_data: "bytes"
    """<p>The x509 v3 specified certificate revocation list (CRL).</p>"""
    enabled: NotRequired["bool"]
    """<p>Specifies whether the certificate revocation list (CRL) is enabled.</p>"""
    tags: NotRequired["capo_rolesanywhere.types.tag_list.TagList"]
    """<p>A list of tags to attach to the certificate revocation list (CRL).</p>"""
    trust_anchor_arn: "capo_rolesanywhere.types.trust_anchor_arn.TrustAnchorArn"
    """<p>The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportCrlRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_rolesanywhere.types._prelude.blob

    out["crlData"] = capo_rolesanywhere.types._prelude.blob.serialize_json(
        value["crl_data"]
    )
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "tags" in value:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.serialize_json(value["tags"])
    out["trustAnchorArn"] = value["trust_anchor_arn"]
    return out


def deserialize_json(data: dict) -> ImportCrlRequest:
    out: ImportCrlRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ImportCrlRequest.name required")
    if "crlData" in data:
        import capo_rolesanywhere.types._prelude.blob

        out["crl_data"] = capo_rolesanywhere.types._prelude.blob.deserialize_json(
            data["crlData"]
        )
    else:
        raise DeserializationError("ImportCrlRequest.crl_data required")
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "tags" in data:
        import capo_rolesanywhere.types.tag_list

        out["tags"] = capo_rolesanywhere.types.tag_list.deserialize_json(data["tags"])
    if "trustAnchorArn" in data:
        out["trust_anchor_arn"] = data["trustAnchorArn"]
    else:
        raise DeserializationError("ImportCrlRequest.trust_anchor_arn required")
    return out
