"""Generated from Smithy shape ``com.amazonaws.acmpca#OcspConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.boolean
    import aws_sdk_acm_pca.types.cname_string


class OcspConfiguration(TypedDict, closed=True):
    enabled: "aws_sdk_acm_pca.types.boolean.Boolean"
    """<p>Flag enabling use of the Online Certificate Status Protocol (OCSP) for validating certificate revocation status.</p>"""
    ocsp_custom_cname: NotRequired["aws_sdk_acm_pca.types.cname_string.CnameString"]
    r"""<p>By default, Amazon Web Services Private CA injects an Amazon Web Services domain into certificates being validated by the Online Certificate Status Protocol (OCSP). A customer can alternatively use this object to define a CNAME specifying a customized OCSP domain.</p> <note> <p>The content of a Canonical Name (CNAME) record must conform to <a href=\"https://www.ietf.org/rfc/rfc2396.txt\">RFC2396</a> restrictions on the use of special characters in URIs. Additionally, the value of the CNAME must not include a protocol prefix such as \"http://\" or \"https://\".</p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/privateca/latest/userguide/ocsp-customize.html\">Customizing Online Certificate Status Protocol (OCSP) </a> in the <i>Amazon Web Services Private Certificate Authority User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OcspConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "ocsp_custom_cname" in value:
        out["OcspCustomCname"] = value["ocsp_custom_cname"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OcspConfiguration:
    out: OcspConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("OcspConfiguration.enabled required")
    if "OcspCustomCname" in data:
        out["ocsp_custom_cname"] = data["OcspCustomCname"]
    return out
