"""Generated from Smithy shape ``com.amazonaws.transfer#ListedServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.arn
    import aws_sdk_transfer.types.domain
    import aws_sdk_transfer.types.endpoint_type
    import aws_sdk_transfer.types.identity_provider_type
    import aws_sdk_transfer.types.role
    import aws_sdk_transfer.types.server_id
    import aws_sdk_transfer.types.state
    import aws_sdk_transfer.types.user_count


class ListedServer(TypedDict, closed=True):
    arn: "aws_sdk_transfer.types.arn.Arn"
    """<p>Specifies the unique Amazon Resource Name (ARN) for a server to be listed.</p>"""
    domain: NotRequired["aws_sdk_transfer.types.domain.Domain"]
    """<p>Specifies the domain of the storage system that is used for file transfers. There are two domains available: Amazon Simple Storage Service (Amazon S3) and Amazon Elastic File System (Amazon EFS). The default value is S3.</p>"""
    identity_provider_type: NotRequired[
        "aws_sdk_transfer.types.identity_provider_type.IdentityProviderType"
    ]
    """<p>The mode of authentication for a server. The default value is <code>SERVICE_MANAGED</code>, which allows you to store and access user credentials within the Transfer Family service.</p> <p>Use <code>AWS_DIRECTORY_SERVICE</code> to provide access to Active Directory groups in Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in Amazon Web Services using AD Connector. This option also requires you to provide a Directory ID by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>API_GATEWAY</code> value to integrate with an identity provider of your choosing. The <code>API_GATEWAY</code> setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>AWS_LAMBDA</code> value to directly use an Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the <code>Function</code> parameter for the <code>IdentityProviderDetails</code> data type.</p>"""
    endpoint_type: NotRequired["aws_sdk_transfer.types.endpoint_type.EndpointType"]
    """<p>Specifies the type of VPC endpoint that your server is connected to. If your server is connected to a VPC endpoint, your server isn't accessible over the public internet.</p>"""
    logging_role: NotRequired["aws_sdk_transfer.types.role.Role"]
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFS events. When set, you can view user activity in your CloudWatch logs.</p>"""
    server_id: NotRequired["aws_sdk_transfer.types.server_id.ServerId"]
    """<p>Specifies the unique system assigned identifier for the servers that were listed.</p>"""
    state: NotRequired["aws_sdk_transfer.types.state.State"]
    """<p>The condition of the server that was described. A value of <code>ONLINE</code> indicates that the server can accept jobs and transfer files. A <code>State</code> value of <code>OFFLINE</code> means that the server cannot perform file transfer operations.</p> <p>The states of <code>STARTING</code> and <code>STOPPING</code> indicate that the server is in an intermediate state, either not fully able to respond, or not fully offline. The values of <code>START_FAILED</code> or <code>STOP_FAILED</code> can indicate an error condition.</p>"""
    user_count: NotRequired["aws_sdk_transfer.types.user_count.UserCount"]
    """<p>Specifies the number of users that are assigned to a server you specified with the <code>ServerId</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedServer) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "domain" in value:
        import aws_sdk_transfer.types.domain

        out["Domain"] = aws_sdk_transfer.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
    if "identity_provider_type" in value:
        import aws_sdk_transfer.types.identity_provider_type

        out["IdentityProviderType"] = (
            aws_sdk_transfer.types.identity_provider_type.serialize_aws_json_1_1(
                value["identity_provider_type"]
            )
        )
    if "endpoint_type" in value:
        import aws_sdk_transfer.types.endpoint_type

        out["EndpointType"] = (
            aws_sdk_transfer.types.endpoint_type.serialize_aws_json_1_1(
                value["endpoint_type"]
            )
        )
    if "logging_role" in value:
        out["LoggingRole"] = value["logging_role"]
    if "server_id" in value:
        out["ServerId"] = value["server_id"]
    if "state" in value:
        import aws_sdk_transfer.types.state

        out["State"] = aws_sdk_transfer.types.state.serialize_aws_json_1_1(
            value["state"]
        )
    if "user_count" in value:
        out["UserCount"] = value["user_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListedServer:
    out: ListedServer = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ListedServer.arn required")
    if "Domain" in data:
        import aws_sdk_transfer.types.domain

        out["domain"] = aws_sdk_transfer.types.domain.deserialize_aws_json_1_1(
            data["Domain"]
        )
    if "IdentityProviderType" in data:
        import aws_sdk_transfer.types.identity_provider_type

        out["identity_provider_type"] = (
            aws_sdk_transfer.types.identity_provider_type.deserialize_aws_json_1_1(
                data["IdentityProviderType"]
            )
        )
    if "EndpointType" in data:
        import aws_sdk_transfer.types.endpoint_type

        out["endpoint_type"] = (
            aws_sdk_transfer.types.endpoint_type.deserialize_aws_json_1_1(
                data["EndpointType"]
            )
        )
    if "LoggingRole" in data:
        out["logging_role"] = data["LoggingRole"]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    if "State" in data:
        import aws_sdk_transfer.types.state

        out["state"] = aws_sdk_transfer.types.state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "UserCount" in data:
        out["user_count"] = data["UserCount"]
    return out
