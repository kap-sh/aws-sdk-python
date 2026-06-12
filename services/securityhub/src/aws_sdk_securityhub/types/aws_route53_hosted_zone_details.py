"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRoute53HostedZoneDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_route53_hosted_zone_name_servers_list
    import aws_sdk_securityhub.types.aws_route53_hosted_zone_object_details
    import aws_sdk_securityhub.types.aws_route53_hosted_zone_vpcs_list
    import aws_sdk_securityhub.types.aws_route53_query_logging_config_details


class AwsRoute53HostedZoneDetails(TypedDict):
    hosted_zone: NotRequired[
        "aws_sdk_securityhub.types.aws_route53_hosted_zone_object_details.AwsRoute53HostedZoneObjectDetails"
    ]
    """<p> An object that contains information about the specified hosted zone.</p>"""
    vpcs: NotRequired[
        "aws_sdk_securityhub.types.aws_route53_hosted_zone_vpcs_list.AwsRoute53HostedZoneVpcsList"
    ]
    """<p> An object that contains information about the Amazon Virtual Private Clouds (Amazon VPCs) that are associated with the specified hosted zone.</p>"""
    name_servers: NotRequired[
        "aws_sdk_securityhub.types.aws_route53_hosted_zone_name_servers_list.AwsRoute53HostedZoneNameServersList"
    ]
    """<p> An object that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.</p>"""
    query_logging_config: NotRequired[
        "aws_sdk_securityhub.types.aws_route53_query_logging_config_details.AwsRoute53QueryLoggingConfigDetails"
    ]
    """<p> An array that contains one <code>QueryLoggingConfig</code> element for each DNS query logging configuration that is associated with the current Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRoute53HostedZoneDetails) -> dict:
    out: dict = {}
    if "hosted_zone" in value:
        import aws_sdk_securityhub.types.aws_route53_hosted_zone_object_details

        out["HostedZone"] = (
            aws_sdk_securityhub.types.aws_route53_hosted_zone_object_details.serialize_json(
                value["hosted_zone"]
            )
        )
    if "vpcs" in value:
        import aws_sdk_securityhub.types.aws_route53_hosted_zone_vpcs_list

        out["Vpcs"] = (
            aws_sdk_securityhub.types.aws_route53_hosted_zone_vpcs_list.serialize_json(
                value["vpcs"]
            )
        )
    if "name_servers" in value:
        import aws_sdk_securityhub.types.aws_route53_hosted_zone_name_servers_list

        out["NameServers"] = (
            aws_sdk_securityhub.types.aws_route53_hosted_zone_name_servers_list.serialize_json(
                value["name_servers"]
            )
        )
    if "query_logging_config" in value:
        import aws_sdk_securityhub.types.aws_route53_query_logging_config_details

        out["QueryLoggingConfig"] = (
            aws_sdk_securityhub.types.aws_route53_query_logging_config_details.serialize_json(
                value["query_logging_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsRoute53HostedZoneDetails:
    out: AwsRoute53HostedZoneDetails = {}  # type: ignore[typeddict-item]
    if "HostedZone" in data:
        import aws_sdk_securityhub.types.aws_route53_hosted_zone_object_details

        out["hosted_zone"] = (
            aws_sdk_securityhub.types.aws_route53_hosted_zone_object_details.deserialize_json(
                data["HostedZone"]
            )
        )
    if "Vpcs" in data:
        import aws_sdk_securityhub.types.aws_route53_hosted_zone_vpcs_list

        out["vpcs"] = (
            aws_sdk_securityhub.types.aws_route53_hosted_zone_vpcs_list.deserialize_json(
                data["Vpcs"]
            )
        )
    if "NameServers" in data:
        import aws_sdk_securityhub.types.aws_route53_hosted_zone_name_servers_list

        out["name_servers"] = (
            aws_sdk_securityhub.types.aws_route53_hosted_zone_name_servers_list.deserialize_json(
                data["NameServers"]
            )
        )
    if "QueryLoggingConfig" in data:
        import aws_sdk_securityhub.types.aws_route53_query_logging_config_details

        out["query_logging_config"] = (
            aws_sdk_securityhub.types.aws_route53_query_logging_config_details.deserialize_json(
                data["QueryLoggingConfig"]
            )
        )
    return out
