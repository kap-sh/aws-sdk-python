"""Generated from Smithy shape ``com.amazonaws.configservice#AggregationAuthorizationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregation_authorization

AggregationAuthorizationList: TypeAlias = list[
    "aws_sdk_config_service.types.aggregation_authorization.AggregationAuthorization"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregationAuthorizationList) -> list:
    import aws_sdk_config_service.types.aggregation_authorization

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.aggregation_authorization.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AggregationAuthorizationList:
    import aws_sdk_config_service.types.aggregation_authorization

    out: AggregationAuthorizationList = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.aggregation_authorization.deserialize_aws_json_1_1(
                item
            )
        )
    return out
