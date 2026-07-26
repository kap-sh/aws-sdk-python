"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#AttributeMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.certificate_field
    import capo_rolesanywhere.types.mapping_rules


class AttributeMapping(TypedDict, closed=True):
    certificate_field: NotRequired[
        "capo_rolesanywhere.types.certificate_field.CertificateField"
    ]
    """<p>Fields (x509Subject, x509Issuer and x509SAN) within X.509 certificates.</p>"""
    mapping_rules: NotRequired["capo_rolesanywhere.types.mapping_rules.MappingRules"]
    """<p>A list of mapping entries for every supported specifier or sub-field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeMapping) -> dict:
    out: dict = {}
    if "certificate_field" in value:
        out["certificateField"] = value["certificate_field"]
    if "mapping_rules" in value:
        import capo_rolesanywhere.types.mapping_rules

        out["mappingRules"] = capo_rolesanywhere.types.mapping_rules.serialize_json(
            value["mapping_rules"]
        )
    return out


def deserialize_json(data: dict) -> AttributeMapping:
    out: AttributeMapping = {}  # type: ignore[typeddict-item]
    if "certificateField" in data:
        out["certificate_field"] = data["certificateField"]
    if "mappingRules" in data:
        import capo_rolesanywhere.types.mapping_rules

        out["mapping_rules"] = capo_rolesanywhere.types.mapping_rules.deserialize_json(
            data["mappingRules"]
        )
    return out
