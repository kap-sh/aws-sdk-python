"""Generated from Smithy shape ``com.amazonaws.apprunner#DescribeCustomDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.custom_domain_list
    import aws_sdk_apprunner.types.string
    import aws_sdk_apprunner.types.vpc_dns_target_list


class DescribeCustomDomainsResponse(TypedDict, closed=True):
    dns_target: "aws_sdk_apprunner.types.string.String"
    """<p>The App Runner subdomain of the App Runner service. The associated custom domain names are mapped to this target name.</p>"""
    service_arn: "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the App Runner service whose associated custom domain names you want to describe.</p>"""
    custom_domains: "aws_sdk_apprunner.types.custom_domain_list.CustomDomainList"
    """<p>A list of descriptions of custom domain names that are associated with the service. In a paginated request, the request returns up to <code>MaxResults</code> records per call.</p>"""
    vpc_dns_targets: "aws_sdk_apprunner.types.vpc_dns_target_list.VpcDNSTargetList"
    """<p>DNS Target records for the custom domains of this Amazon VPC. </p>"""
    next_token: NotRequired["aws_sdk_apprunner.types.string.String"]
    """<p>The token that you can pass in a subsequent request to get the next result page. It's returned in a paginated request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeCustomDomainsResponse) -> dict:
    out: dict = {}
    out["DNSTarget"] = value["dns_target"]
    out["ServiceArn"] = value["service_arn"]
    import aws_sdk_apprunner.types.custom_domain_list

    out["CustomDomains"] = (
        aws_sdk_apprunner.types.custom_domain_list.serialize_aws_json_1_0(
            value["custom_domains"]
        )
    )
    import aws_sdk_apprunner.types.vpc_dns_target_list

    out["VpcDNSTargets"] = (
        aws_sdk_apprunner.types.vpc_dns_target_list.serialize_aws_json_1_0(
            value["vpc_dns_targets"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeCustomDomainsResponse:
    out: DescribeCustomDomainsResponse = {}  # type: ignore[typeddict-item]
    if "DNSTarget" in data:
        out["dns_target"] = data["DNSTarget"]
    else:
        raise DeserializationError("DescribeCustomDomainsResponse.dns_target required")
    if "ServiceArn" in data:
        out["service_arn"] = data["ServiceArn"]
    else:
        raise DeserializationError("DescribeCustomDomainsResponse.service_arn required")
    if "CustomDomains" in data:
        import aws_sdk_apprunner.types.custom_domain_list

        out["custom_domains"] = (
            aws_sdk_apprunner.types.custom_domain_list.deserialize_aws_json_1_0(
                data["CustomDomains"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeCustomDomainsResponse.custom_domains required"
        )
    if "VpcDNSTargets" in data:
        import aws_sdk_apprunner.types.vpc_dns_target_list

        out["vpc_dns_targets"] = (
            aws_sdk_apprunner.types.vpc_dns_target_list.deserialize_aws_json_1_0(
                data["VpcDNSTargets"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeCustomDomainsResponse.vpc_dns_targets required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
