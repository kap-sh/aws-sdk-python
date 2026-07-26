"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoClientAuthenticationTlsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.string_list


class AwsMskClusterClusterInfoClientAuthenticationTlsDetails(TypedDict, closed=True):
    certificate_authority_arn_list: NotRequired[
        "capo_securityhub.types.string_list.StringList"
    ]
    """<p> List of Amazon Web Services Private CA Amazon Resource Names (ARNs). Amazon Web Services Private CA enables creation of private certificate authority (CA) hierarchies, including root and subordinate CAs, without the investment and maintenance costs of operating an on-premises CA.</p>"""
    enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether TLS authentication is enabled or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsMskClusterClusterInfoClientAuthenticationTlsDetails,
) -> dict:
    out: dict = {}
    if "certificate_authority_arn_list" in value:
        import capo_securityhub.types.string_list

        out["CertificateAuthorityArnList"] = (
            capo_securityhub.types.string_list.serialize_json(
                value["certificate_authority_arn_list"]
            )
        )
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(
    data: dict,
) -> AwsMskClusterClusterInfoClientAuthenticationTlsDetails:
    out: AwsMskClusterClusterInfoClientAuthenticationTlsDetails = {}  # type: ignore[typeddict-item]
    if "CertificateAuthorityArnList" in data:
        import capo_securityhub.types.string_list

        out["certificate_authority_arn_list"] = (
            capo_securityhub.types.string_list.deserialize_json(
                data["CertificateAuthorityArnList"]
            )
        )
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
