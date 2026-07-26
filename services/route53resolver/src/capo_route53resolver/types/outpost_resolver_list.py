"""Generated from Smithy shape ``com.amazonaws.route53resolver#OutpostResolverList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.outpost_resolver

OutpostResolverList: TypeAlias = list[
    "capo_route53resolver.types.outpost_resolver.OutpostResolver"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutpostResolverList) -> list:
    import capo_route53resolver.types.outpost_resolver

    out: list = []
    for item in value:
        out.append(
            capo_route53resolver.types.outpost_resolver.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OutpostResolverList:
    import capo_route53resolver.types.outpost_resolver

    out: OutpostResolverList = []
    for item in data:
        out.append(
            capo_route53resolver.types.outpost_resolver.deserialize_aws_json_1_1(item)
        )
    return out
