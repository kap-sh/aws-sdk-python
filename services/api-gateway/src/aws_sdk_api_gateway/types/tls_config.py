"""Generated from Smithy shape ``com.amazonaws.apigateway#TlsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.boolean


class TlsConfig(TypedDict, closed=True):
    insecure_skip_verification: "aws_sdk_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether or not API Gateway skips verification that the certificate for an integration endpoint is issued by a supported certificate authority. This isn’t recommended, but it enables you to use certificates that are signed by private certificate authorities, or certificates that are self-signed. If enabled, API Gateway still performs basic certificate validation, which includes checking the certificate's expiration date, hostname, and presence of a root certificate authority. Supported only for <code>HTTP</code> and <code>HTTP_PROXY</code> integrations.</p> <important> <p>Enabling <code>insecureSkipVerification</code> isn't recommended, especially for integrations with public HTTPS endpoints. If you enable <code>insecureSkipVerification</code>, you increase the risk of man-in-the-middle attacks.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: TlsConfig) -> dict:
    out: dict = {}
    out["insecureSkipVerification"] = value.get("insecure_skip_verification", False)
    return out


def deserialize_json(data: dict) -> TlsConfig:
    out: TlsConfig = {}  # type: ignore[typeddict-item]
    if "insecureSkipVerification" in data:
        out["insecure_skip_verification"] = data["insecureSkipVerification"]
    else:
        out["insecure_skip_verification"] = False
    return out
