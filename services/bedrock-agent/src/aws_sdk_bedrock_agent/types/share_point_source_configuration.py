"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SharePointSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.microsoft365_tenant_id
    import aws_sdk_bedrock_agent.types.secret_arn
    import aws_sdk_bedrock_agent.types.share_point_auth_type
    import aws_sdk_bedrock_agent.types.share_point_domain
    import aws_sdk_bedrock_agent.types.share_point_host_type
    import aws_sdk_bedrock_agent.types.share_point_site_urls


class SharePointSourceConfiguration(TypedDict, closed=True):
    tenant_id: NotRequired[
        "aws_sdk_bedrock_agent.types.microsoft365_tenant_id.Microsoft365TenantId"
    ]
    """<p>The identifier of your Microsoft 365 tenant.</p>"""
    domain: "aws_sdk_bedrock_agent.types.share_point_domain.SharePointDomain"
    """<p>The domain of your SharePoint instance or site URL/URLs.</p>"""
    site_urls: "aws_sdk_bedrock_agent.types.share_point_site_urls.SharePointSiteUrls"
    """<p>A list of one or more SharePoint site URLs.</p>"""
    host_type: "aws_sdk_bedrock_agent.types.share_point_host_type.SharePointHostType"
    """<p>The supported host type, whether online/cloud or server/on-premises.</p>"""
    auth_type: "aws_sdk_bedrock_agent.types.share_point_auth_type.SharePointAuthType"
    """<p>The supported authentication type to authenticate and connect to your SharePoint site/sites.</p>"""
    credentials_secret_arn: "aws_sdk_bedrock_agent.types.secret_arn.SecretArn"
    r"""<p>The Amazon Resource Name of an Secrets Manager secret that stores your authentication credentials for your SharePoint site/sites. For more information on the key-value pairs that must be included in your secret, depending on your authentication type, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/sharepoint-data-source-connector.html#configuration-sharepoint-connector\">SharePoint connection configuration</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharePointSourceConfiguration) -> dict:
    out: dict = {}
    if "tenant_id" in value:
        out["tenantId"] = value["tenant_id"]
    out["domain"] = value["domain"]
    import aws_sdk_bedrock_agent.types.share_point_site_urls

    out["siteUrls"] = aws_sdk_bedrock_agent.types.share_point_site_urls.serialize_json(
        value["site_urls"]
    )
    import aws_sdk_bedrock_agent.types.share_point_host_type

    out["hostType"] = aws_sdk_bedrock_agent.types.share_point_host_type.serialize_json(
        value["host_type"]
    )
    import aws_sdk_bedrock_agent.types.share_point_auth_type

    out["authType"] = aws_sdk_bedrock_agent.types.share_point_auth_type.serialize_json(
        value["auth_type"]
    )
    out["credentialsSecretArn"] = value["credentials_secret_arn"]
    return out


def deserialize_json(data: dict) -> SharePointSourceConfiguration:
    out: SharePointSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "tenantId" in data:
        out["tenant_id"] = data["tenantId"]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("SharePointSourceConfiguration.domain required")
    if "siteUrls" in data:
        import aws_sdk_bedrock_agent.types.share_point_site_urls

        out["site_urls"] = (
            aws_sdk_bedrock_agent.types.share_point_site_urls.deserialize_json(
                data["siteUrls"]
            )
        )
    else:
        raise DeserializationError("SharePointSourceConfiguration.site_urls required")
    if "hostType" in data:
        import aws_sdk_bedrock_agent.types.share_point_host_type

        out["host_type"] = (
            aws_sdk_bedrock_agent.types.share_point_host_type.deserialize_json(
                data["hostType"]
            )
        )
    else:
        raise DeserializationError("SharePointSourceConfiguration.host_type required")
    if "authType" in data:
        import aws_sdk_bedrock_agent.types.share_point_auth_type

        out["auth_type"] = (
            aws_sdk_bedrock_agent.types.share_point_auth_type.deserialize_json(
                data["authType"]
            )
        )
    else:
        raise DeserializationError("SharePointSourceConfiguration.auth_type required")
    if "credentialsSecretArn" in data:
        out["credentials_secret_arn"] = data["credentialsSecretArn"]
    else:
        raise DeserializationError(
            "SharePointSourceConfiguration.credentials_secret_arn required"
        )
    return out
