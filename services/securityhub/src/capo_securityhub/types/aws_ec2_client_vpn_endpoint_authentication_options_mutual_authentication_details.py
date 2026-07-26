"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetails(
    TypedDict, closed=True
):
    client_root_certificate_chain: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the client certificate. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetails,
) -> dict:
    out: dict = {}
    if "client_root_certificate_chain" in value:
        out["ClientRootCertificateChain"] = value["client_root_certificate_chain"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetails:
    out: AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetails = {}  # type: ignore[typeddict-item]
    if "ClientRootCertificateChain" in data:
        out["client_root_certificate_chain"] = data["ClientRootCertificateChain"]
    return out
