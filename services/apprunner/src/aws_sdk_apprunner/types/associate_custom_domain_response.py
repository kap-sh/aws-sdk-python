"""Generated from Smithy shape ``com.amazonaws.apprunner#AssociateCustomDomainResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.custom_domain
    import aws_sdk_apprunner.types.string
    import aws_sdk_apprunner.types.vpc_dns_target_list


class AssociateCustomDomainResponse(TypedDict):
    dns_target: "aws_sdk_apprunner.types.string.String"
    """<p>The App Runner subdomain of the App Runner service. The custom domain name is mapped to this target name.</p>"""
    service_arn: "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of the App Runner service with which a custom domain name is associated.</p>"""
    custom_domain: "aws_sdk_apprunner.types.custom_domain.CustomDomain"
    """<p>A description of the domain name that's being associated.</p>"""
    vpc_dns_targets: "aws_sdk_apprunner.types.vpc_dns_target_list.VpcDNSTargetList"
    """<p>DNS Target records for the custom domains of this Amazon VPC. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateCustomDomainResponse) -> dict:
    out: dict = {}
    out["DNSTarget"] = value["dns_target"]
    out["ServiceArn"] = value["service_arn"]
    import aws_sdk_apprunner.types.custom_domain

    out["CustomDomain"] = aws_sdk_apprunner.types.custom_domain.serialize_aws_json_1_0(
        value["custom_domain"]
    )
    import aws_sdk_apprunner.types.vpc_dns_target_list

    out["VpcDNSTargets"] = (
        aws_sdk_apprunner.types.vpc_dns_target_list.serialize_aws_json_1_0(
            value["vpc_dns_targets"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateCustomDomainResponse:
    out: AssociateCustomDomainResponse = {}  # type: ignore[typeddict-item]
    if "DNSTarget" in data:
        out["dns_target"] = data["DNSTarget"]
    else:
        raise DeserializationError("AssociateCustomDomainResponse.dns_target required")
    if "ServiceArn" in data:
        out["service_arn"] = data["ServiceArn"]
    else:
        raise DeserializationError("AssociateCustomDomainResponse.service_arn required")
    if "CustomDomain" in data:
        import aws_sdk_apprunner.types.custom_domain

        out["custom_domain"] = (
            aws_sdk_apprunner.types.custom_domain.deserialize_aws_json_1_0(
                data["CustomDomain"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateCustomDomainResponse.custom_domain required"
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
            "AssociateCustomDomainResponse.vpc_dns_targets required"
        )
    return out
