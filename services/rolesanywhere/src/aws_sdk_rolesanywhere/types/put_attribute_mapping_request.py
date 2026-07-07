"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#PutAttributeMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rolesanywhere.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.certificate_field
    import aws_sdk_rolesanywhere.types.mapping_rules
    import aws_sdk_rolesanywhere.types.uuid


class PutAttributeMappingRequest(TypedDict, closed=True):
    profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid"
    """<p>The unique identifier of the profile.</p>"""
    certificate_field: "aws_sdk_rolesanywhere.types.certificate_field.CertificateField"
    """<p>Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.</p>"""
    mapping_rules: "aws_sdk_rolesanywhere.types.mapping_rules.MappingRules"
    """<p>A list of mapping entries for every supported specifier or sub-field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAttributeMappingRequest) -> dict:
    out: dict = {}
    out["certificateField"] = value["certificate_field"]
    import aws_sdk_rolesanywhere.types.mapping_rules

    out["mappingRules"] = aws_sdk_rolesanywhere.types.mapping_rules.serialize_json(
        value["mapping_rules"]
    )
    return out


def deserialize_json(data: dict) -> PutAttributeMappingRequest:
    out: PutAttributeMappingRequest = {}  # type: ignore[typeddict-item]
    if "certificateField" in data:
        out["certificate_field"] = data["certificateField"]
    else:
        raise DeserializationError(
            "PutAttributeMappingRequest.certificate_field required"
        )
    if "mappingRules" in data:
        import aws_sdk_rolesanywhere.types.mapping_rules

        out["mapping_rules"] = (
            aws_sdk_rolesanywhere.types.mapping_rules.deserialize_json(
                data["mappingRules"]
            )
        )
    else:
        raise DeserializationError("PutAttributeMappingRequest.mapping_rules required")
    return out
