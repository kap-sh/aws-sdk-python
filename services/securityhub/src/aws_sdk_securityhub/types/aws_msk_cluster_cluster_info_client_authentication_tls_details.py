"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoClientAuthenticationTlsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.string_list


class AwsMskClusterClusterInfoClientAuthenticationTlsDetails(TypedDict):
    certificate_authority_arn_list: NotRequired[
        "aws_sdk_securityhub.types.string_list.StringList"
    ]
    """<p> List of Amazon Web Services Private CA Amazon Resource Names (ARNs). Amazon Web Services Private CA enables creation of private certificate authority (CA) hierarchies, including root and subordinate CAs, without the investment and maintenance costs of operating an on-premises CA.</p>"""
    enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether TLS authentication is enabled or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsMskClusterClusterInfoClientAuthenticationTlsDetails,
) -> dict:
    out: dict = {}
    if "certificate_authority_arn_list" in value:
        import aws_sdk_securityhub.types.string_list

        out["CertificateAuthorityArnList"] = (
            aws_sdk_securityhub.types.string_list.serialize_json(
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
        import aws_sdk_securityhub.types.string_list

        out["certificate_authority_arn_list"] = (
            aws_sdk_securityhub.types.string_list.deserialize_json(
                data["CertificateAuthorityArnList"]
            )
        )
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
