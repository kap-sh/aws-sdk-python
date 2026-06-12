"""Generated from Smithy shape ``com.amazonaws.route53resolver#Filters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.filter

Filters: TypeAlias = list["aws_sdk_route53resolver.types.filter.Filter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filters) -> list:
    import aws_sdk_route53resolver.types.filter

    out: list = []
    for item in value:
        out.append(aws_sdk_route53resolver.types.filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Filters:
    import aws_sdk_route53resolver.types.filter

    out: Filters = []
    for item in data:
        out.append(aws_sdk_route53resolver.types.filter.deserialize_aws_json_1_1(item))
    return out
