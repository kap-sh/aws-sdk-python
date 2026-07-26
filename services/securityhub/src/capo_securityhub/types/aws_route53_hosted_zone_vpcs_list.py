"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRoute53HostedZoneVpcsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_route53_hosted_zone_vpc_details

AwsRoute53HostedZoneVpcsList: TypeAlias = list[
    "capo_securityhub.types.aws_route53_hosted_zone_vpc_details.AwsRoute53HostedZoneVpcDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRoute53HostedZoneVpcsList) -> list:
    import capo_securityhub.types.aws_route53_hosted_zone_vpc_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_route53_hosted_zone_vpc_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsRoute53HostedZoneVpcsList:
    import capo_securityhub.types.aws_route53_hosted_zone_vpc_details

    out: AwsRoute53HostedZoneVpcsList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_route53_hosted_zone_vpc_details.deserialize_json(
                item
            )
        )
    return out
