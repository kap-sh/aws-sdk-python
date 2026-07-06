"""Generated from Smithy shape ``com.amazonaws.acmpca#OtherName``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.custom_object_identifier
    import aws_sdk_acm_pca.types.string256


class OtherName(TypedDict, closed=True):
    type_id: "aws_sdk_acm_pca.types.custom_object_identifier.CustomObjectIdentifier"
    """<p>Specifies an OID. </p>"""
    value: "aws_sdk_acm_pca.types.string256.String256"
    """<p>Specifies an OID value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OtherName) -> dict:
    out: dict = {}
    out["TypeId"] = value["type_id"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OtherName:
    out: OtherName = {}  # type: ignore[typeddict-item]
    if "TypeId" in data:
        out["type_id"] = data["TypeId"]
    else:
        raise DeserializationError("OtherName.type_id required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("OtherName.value required")
    return out
