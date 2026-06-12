"""Generated from Smithy shape ``com.amazonaws.apprunner#AssociateCustomDomainRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.domain_name
    import aws_sdk_apprunner.types.nullable_boolean


class AssociateCustomDomainRequest(TypedDict):
    service_arn: "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the App Runner service that you want to associate a custom domain name with.</p>"""
    domain_name: "aws_sdk_apprunner.types.domain_name.DomainName"
    """<p>A custom domain endpoint to associate. Specify a root domain (for example, <code>example.com</code>), a subdomain (for example, <code>login.example.com</code> or <code>admin.login.example.com</code>), or a wildcard (for example, <code>*.example.com</code>).</p>"""
    enable_www_subdomain: NotRequired[
        "aws_sdk_apprunner.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Set to <code>true</code> to associate the subdomain <code>www.<i>DomainName</i> </code> with the App Runner service in addition to the base domain.</p> <p>Default: <code>true</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateCustomDomainRequest) -> dict:
    out: dict = {}
    out["ServiceArn"] = value["service_arn"]
    out["DomainName"] = value["domain_name"]
    if "enable_www_subdomain" in value:
        out["EnableWWWSubdomain"] = value["enable_www_subdomain"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateCustomDomainRequest:
    out: AssociateCustomDomainRequest = {}  # type: ignore[typeddict-item]
    if "ServiceArn" in data:
        out["service_arn"] = data["ServiceArn"]
    else:
        raise DeserializationError("AssociateCustomDomainRequest.service_arn required")
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("AssociateCustomDomainRequest.domain_name required")
    if "EnableWWWSubdomain" in data:
        out["enable_www_subdomain"] = data["EnableWWWSubdomain"]
    return out
