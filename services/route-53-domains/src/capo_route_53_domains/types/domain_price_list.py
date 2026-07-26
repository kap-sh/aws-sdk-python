"""Generated from Smithy shape ``com.amazonaws.route53domains#DomainPriceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_price

DomainPriceList: TypeAlias = list[
    "capo_route_53_domains.types.domain_price.DomainPrice"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainPriceList) -> list:
    import capo_route_53_domains.types.domain_price

    out: list = []
    for item in value:
        out.append(
            capo_route_53_domains.types.domain_price.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DomainPriceList:
    import capo_route_53_domains.types.domain_price

    out: DomainPriceList = []
    for item in data:
        out.append(
            capo_route_53_domains.types.domain_price.deserialize_aws_json_1_1(item)
        )
    return out
