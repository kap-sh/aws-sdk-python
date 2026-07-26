"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRoute53HostedZoneDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_route53_hosted_zone_name_servers_list
    import capo_securityhub.types.aws_route53_hosted_zone_object_details
    import capo_securityhub.types.aws_route53_hosted_zone_vpcs_list
    import capo_securityhub.types.aws_route53_query_logging_config_details


class AwsRoute53HostedZoneDetails(TypedDict, closed=True):
    hosted_zone: NotRequired[
        "capo_securityhub.types.aws_route53_hosted_zone_object_details.AwsRoute53HostedZoneObjectDetails"
    ]
    """<p> An object that contains information about the specified hosted zone.</p>"""
    vpcs: NotRequired[
        "capo_securityhub.types.aws_route53_hosted_zone_vpcs_list.AwsRoute53HostedZoneVpcsList"
    ]
    """<p> An object that contains information about the Amazon Virtual Private Clouds (Amazon VPCs) that are associated with the specified hosted zone.</p>"""
    name_servers: NotRequired[
        "capo_securityhub.types.aws_route53_hosted_zone_name_servers_list.AwsRoute53HostedZoneNameServersList"
    ]
    """<p> An object that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.</p>"""
    query_logging_config: NotRequired[
        "capo_securityhub.types.aws_route53_query_logging_config_details.AwsRoute53QueryLoggingConfigDetails"
    ]
    """<p> An array that contains one <code>QueryLoggingConfig</code> element for each DNS query logging configuration that is associated with the current Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRoute53HostedZoneDetails) -> dict:
    out: dict = {}
    if "hosted_zone" in value:
        import capo_securityhub.types.aws_route53_hosted_zone_object_details

        out["HostedZone"] = (
            capo_securityhub.types.aws_route53_hosted_zone_object_details.serialize_json(
                value["hosted_zone"]
            )
        )
    if "vpcs" in value:
        import capo_securityhub.types.aws_route53_hosted_zone_vpcs_list

        out["Vpcs"] = (
            capo_securityhub.types.aws_route53_hosted_zone_vpcs_list.serialize_json(
                value["vpcs"]
            )
        )
    if "name_servers" in value:
        import capo_securityhub.types.aws_route53_hosted_zone_name_servers_list

        out["NameServers"] = (
            capo_securityhub.types.aws_route53_hosted_zone_name_servers_list.serialize_json(
                value["name_servers"]
            )
        )
    if "query_logging_config" in value:
        import capo_securityhub.types.aws_route53_query_logging_config_details

        out["QueryLoggingConfig"] = (
            capo_securityhub.types.aws_route53_query_logging_config_details.serialize_json(
                value["query_logging_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsRoute53HostedZoneDetails:
    out: AwsRoute53HostedZoneDetails = {}  # type: ignore[typeddict-item]
    if "HostedZone" in data:
        import capo_securityhub.types.aws_route53_hosted_zone_object_details

        out["hosted_zone"] = (
            capo_securityhub.types.aws_route53_hosted_zone_object_details.deserialize_json(
                data["HostedZone"]
            )
        )
    if "Vpcs" in data:
        import capo_securityhub.types.aws_route53_hosted_zone_vpcs_list

        out["vpcs"] = (
            capo_securityhub.types.aws_route53_hosted_zone_vpcs_list.deserialize_json(
                data["Vpcs"]
            )
        )
    if "NameServers" in data:
        import capo_securityhub.types.aws_route53_hosted_zone_name_servers_list

        out["name_servers"] = (
            capo_securityhub.types.aws_route53_hosted_zone_name_servers_list.deserialize_json(
                data["NameServers"]
            )
        )
    if "QueryLoggingConfig" in data:
        import capo_securityhub.types.aws_route53_query_logging_config_details

        out["query_logging_config"] = (
            capo_securityhub.types.aws_route53_query_logging_config_details.deserialize_json(
                data["QueryLoggingConfig"]
            )
        )
    return out
