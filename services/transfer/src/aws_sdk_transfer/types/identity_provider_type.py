"""Generated from Smithy shape ``com.amazonaws.transfer#IdentityProviderType``."""

from typing import Literal, TypeAlias, cast

"""<p>The mode of authentication for a server. The default value is <code>SERVICE_MANAGED</code>, which allows you to store and access user credentials within the Transfer Family service.</p> <p>Use <code>AWS_DIRECTORY_SERVICE</code> to provide access to Active Directory groups in Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in Amazon Web Services using AD Connector. This option also requires you to provide a Directory ID by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>API_GATEWAY</code> value to integrate with an identity provider of your choosing. The <code>API_GATEWAY</code> setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>AWS_LAMBDA</code> value to directly use an Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the <code>Function</code> parameter for the <code>IdentityProviderDetails</code> data type.</p>"""
IdentityProviderType: TypeAlias = Literal[
    "SERVICE_MANAGED",
    "API_GATEWAY",
    "AWS_DIRECTORY_SERVICE",
    "AWS_LAMBDA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityProviderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IdentityProviderType:
    return cast(IdentityProviderType, data)
