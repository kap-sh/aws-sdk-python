"""Generated from Smithy shape ``com.amazonaws.route53domains#FilterConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.filter_condition

FilterConditions: TypeAlias = list[
    "aws_sdk_route_53_domains.types.filter_condition.FilterCondition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterConditions) -> list:
    import aws_sdk_route_53_domains.types.filter_condition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route_53_domains.types.filter_condition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FilterConditions:
    import aws_sdk_route_53_domains.types.filter_condition

    out: FilterConditions = []
    for item in data:
        out.append(
            aws_sdk_route_53_domains.types.filter_condition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
