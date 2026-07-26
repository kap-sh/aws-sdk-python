"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#DeleteAttributeMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.certificate_field
    import capo_rolesanywhere.types.specifier_list
    import capo_rolesanywhere.types.uuid


class DeleteAttributeMappingRequest(TypedDict, closed=True):
    profile_id: "capo_rolesanywhere.types.uuid.Uuid"
    """<p>The unique identifier of the profile.</p>"""
    certificate_field: "capo_rolesanywhere.types.certificate_field.CertificateField"
    """<p>Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.</p>"""
    specifiers: NotRequired["capo_rolesanywhere.types.specifier_list.SpecifierList"]
    """<p>A list of specifiers of a certificate field; for example, CN, OU, UID from a Subject.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAttributeMappingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAttributeMappingRequest:
    out: DeleteAttributeMappingRequest = {}  # type: ignore[typeddict-item]
    return out
