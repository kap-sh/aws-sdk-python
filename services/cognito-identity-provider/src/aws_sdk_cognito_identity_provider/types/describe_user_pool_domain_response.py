"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeUserPoolDomainResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.domain_description_type


class DescribeUserPoolDomainResponse(TypedDict):
    domain_description: NotRequired[
        "aws_sdk_cognito_identity_provider.types.domain_description_type.DomainDescriptionType"
    ]
    """<p>The details of the requested user pool domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserPoolDomainResponse) -> dict:
    out: dict = {}
    if "domain_description" in value:
        import aws_sdk_cognito_identity_provider.types.domain_description_type

        out["DomainDescription"] = (
            aws_sdk_cognito_identity_provider.types.domain_description_type.serialize_aws_json_1_1(
                value["domain_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserPoolDomainResponse:
    out: DescribeUserPoolDomainResponse = {}  # type: ignore[typeddict-item]
    if "DomainDescription" in data:
        import aws_sdk_cognito_identity_provider.types.domain_description_type

        out["domain_description"] = (
            aws_sdk_cognito_identity_provider.types.domain_description_type.deserialize_aws_json_1_1(
                data["DomainDescription"]
            )
        )
    return out
