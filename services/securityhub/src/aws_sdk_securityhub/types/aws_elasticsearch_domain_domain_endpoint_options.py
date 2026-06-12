"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElasticsearchDomainDomainEndpointOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsElasticsearchDomainDomainEndpointOptions(TypedDict):
    enforce_https: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to require that all traffic to the domain arrive over HTTPS.</p>"""
    tls_security_policy: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The TLS security policy to apply to the HTTPS endpoint of the OpenSearch domain.</p> <p>Valid values:</p> <ul> <li> <p> <code>Policy-Min-TLS-1-0-2019-07</code>, which supports TLSv1.0 and higher</p> </li> <li> <p> <code>Policy-Min-TLS-1-2-2019-07</code>, which only supports TLSv1.2</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElasticsearchDomainDomainEndpointOptions) -> dict:
    out: dict = {}
    if "enforce_https" in value:
        out["EnforceHTTPS"] = value["enforce_https"]
    if "tls_security_policy" in value:
        out["TLSSecurityPolicy"] = value["tls_security_policy"]
    return out


def deserialize_json(data: dict) -> AwsElasticsearchDomainDomainEndpointOptions:
    out: AwsElasticsearchDomainDomainEndpointOptions = {}  # type: ignore[typeddict-item]
    if "EnforceHTTPS" in data:
        out["enforce_https"] = data["EnforceHTTPS"]
    if "TLSSecurityPolicy" in data:
        out["tls_security_policy"] = data["TLSSecurityPolicy"]
    return out
