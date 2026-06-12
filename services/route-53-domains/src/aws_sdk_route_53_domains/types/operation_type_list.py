"""Generated from Smithy shape ``com.amazonaws.route53domains#OperationTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.operation_type

OperationTypeList: TypeAlias = list[
    "aws_sdk_route_53_domains.types.operation_type.OperationType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationTypeList) -> list:
    import aws_sdk_route_53_domains.types.operation_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route_53_domains.types.operation_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OperationTypeList:
    import aws_sdk_route_53_domains.types.operation_type

    out: OperationTypeList = []
    for item in data:
        out.append(
            aws_sdk_route_53_domains.types.operation_type.deserialize_aws_json_1_1(item)
        )
    return out
