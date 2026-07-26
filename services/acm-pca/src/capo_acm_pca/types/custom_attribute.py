"""Generated from Smithy shape ``com.amazonaws.acmpca#CustomAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.custom_object_identifier
    import capo_acm_pca.types.string1_to256


class CustomAttribute(TypedDict, closed=True):
    object_identifier: (
        "capo_acm_pca.types.custom_object_identifier.CustomObjectIdentifier"
    )
    """<p>Specifies the object identifier (OID) of the attribute type of the relative distinguished name (RDN).</p>"""
    value: "capo_acm_pca.types.string1_to256.String1To256"
    """<p/> <p>Specifies the attribute value of relative distinguished name (RDN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomAttribute) -> dict:
    out: dict = {}
    out["ObjectIdentifier"] = value["object_identifier"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomAttribute:
    out: CustomAttribute = {}  # type: ignore[typeddict-item]
    if "ObjectIdentifier" in data:
        out["object_identifier"] = data["ObjectIdentifier"]
    else:
        raise DeserializationError("CustomAttribute.object_identifier required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("CustomAttribute.value required")
    return out
