"""Generated from Smithy shape ``com.amazonaws.route53domains#OperationStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.operation_status

OperationStatusList: TypeAlias = list[
    "aws_sdk_route_53_domains.types.operation_status.OperationStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationStatusList) -> list:
    import aws_sdk_route_53_domains.types.operation_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route_53_domains.types.operation_status.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OperationStatusList:
    import aws_sdk_route_53_domains.types.operation_status

    out: OperationStatusList = []
    for item in data:
        out.append(
            aws_sdk_route_53_domains.types.operation_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
