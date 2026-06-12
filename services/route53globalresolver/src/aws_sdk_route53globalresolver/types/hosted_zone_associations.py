"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#HostedZoneAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.hosted_zone_association_summary

HostedZoneAssociations: TypeAlias = list[
    "aws_sdk_route53globalresolver.types.hosted_zone_association_summary.HostedZoneAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: HostedZoneAssociations) -> list:
    import aws_sdk_route53globalresolver.types.hosted_zone_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53globalresolver.types.hosted_zone_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HostedZoneAssociations:
    import aws_sdk_route53globalresolver.types.hosted_zone_association_summary

    out: HostedZoneAssociations = []
    for item in data:
        out.append(
            aws_sdk_route53globalresolver.types.hosted_zone_association_summary.deserialize_json(
                item
            )
        )
    return out
