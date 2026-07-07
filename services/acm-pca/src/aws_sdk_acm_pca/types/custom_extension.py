"""Generated from Smithy shape ``com.amazonaws.acmpca#CustomExtension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.base64_string1_to4096
    import aws_sdk_acm_pca.types.boolean
    import aws_sdk_acm_pca.types.custom_object_identifier


class CustomExtension(TypedDict, closed=True):
    object_identifier: (
        "aws_sdk_acm_pca.types.custom_object_identifier.CustomObjectIdentifier"
    )
    r"""<p/> <p>Specifies the object identifier (OID) of the X.509 extension. For more information, see the <a href=\"https://oidref.com/2.5.29\">Global OID reference database.</a> </p>"""
    value: "aws_sdk_acm_pca.types.base64_string1_to4096.Base64String1To4096"
    """<p/> <p>Specifies the base64-encoded value of the X.509 extension.</p>"""
    critical: NotRequired["aws_sdk_acm_pca.types.boolean.Boolean"]
    """<p/> <p>Specifies the critical flag of the X.509 extension.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomExtension) -> dict:
    out: dict = {}
    out["ObjectIdentifier"] = value["object_identifier"]
    out["Value"] = value["value"]
    if "critical" in value:
        out["Critical"] = value["critical"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomExtension:
    out: CustomExtension = {}  # type: ignore[typeddict-item]
    if "ObjectIdentifier" in data:
        out["object_identifier"] = data["ObjectIdentifier"]
    else:
        raise DeserializationError("CustomExtension.object_identifier required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("CustomExtension.value required")
    if "Critical" in data:
        out["critical"] = data["Critical"]
    return out
