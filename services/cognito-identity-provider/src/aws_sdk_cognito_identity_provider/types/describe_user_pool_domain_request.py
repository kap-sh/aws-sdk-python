"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeUserPoolDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.domain_type


class DescribeUserPoolDomainRequest(TypedDict, closed=True):
    domain: "aws_sdk_cognito_identity_provider.types.domain_type.DomainType"
    """<p>The domain that you want to describe. For custom domains, this is the fully-qualified domain name, such as <code>auth.example.com</code>. For Amazon Cognito prefix domains, this is the prefix alone, such as <code>auth</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserPoolDomainRequest) -> dict:
    out: dict = {}
    out["Domain"] = value["domain"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserPoolDomainRequest:
    out: DescribeUserPoolDomainRequest = {}  # type: ignore[typeddict-item]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    else:
        raise DeserializationError("DescribeUserPoolDomainRequest.domain required")
    return out
