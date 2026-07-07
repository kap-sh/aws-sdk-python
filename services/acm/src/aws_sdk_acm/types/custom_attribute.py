"""Generated from Smithy shape ``com.amazonaws.acm#CustomAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_acm.types.string


class CustomAttribute(TypedDict, closed=True):
    object_identifier: NotRequired["aws_sdk_acm.types.string.String"]
    """<p>Specifies the object identifier (OID) of the attribute type of the relative distinguished name (RDN).</p>"""
    value: NotRequired["aws_sdk_acm.types.string.String"]
    """<p>Specifies the attribute value of relative distinguished name (RDN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomAttribute) -> dict:
    out: dict = {}
    if "object_identifier" in value:
        out["ObjectIdentifier"] = value["object_identifier"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomAttribute:
    out: CustomAttribute = {}  # type: ignore[typeddict-item]
    if "ObjectIdentifier" in data:
        out["object_identifier"] = data["ObjectIdentifier"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
