"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeUserPoolDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.domain_description_type


class DescribeUserPoolDomainResponse(TypedDict, closed=True):
    domain_description: NotRequired[
        "capo_cognito_identity_provider.types.domain_description_type.DomainDescriptionType"
    ]
    """<p>The details of the requested user pool domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUserPoolDomainResponse) -> dict:
    out: dict = {}
    if "domain_description" in value:
        import capo_cognito_identity_provider.types.domain_description_type

        out["DomainDescription"] = (
            capo_cognito_identity_provider.types.domain_description_type.serialize_aws_json_1_1(
                value["domain_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUserPoolDomainResponse:
    out: DescribeUserPoolDomainResponse = {}  # type: ignore[typeddict-item]
    if "DomainDescription" in data:
        import capo_cognito_identity_provider.types.domain_description_type

        out["domain_description"] = (
            capo_cognito_identity_provider.types.domain_description_type.deserialize_aws_json_1_1(
                data["DomainDescription"]
            )
        )
    return out
