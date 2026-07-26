"""Generated from Smithy shape ``com.amazonaws.configservice#PendingAggregationRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.pending_aggregation_request

PendingAggregationRequestList: TypeAlias = list[
    "capo_config_service.types.pending_aggregation_request.PendingAggregationRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingAggregationRequestList) -> list:
    import capo_config_service.types.pending_aggregation_request

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.pending_aggregation_request.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PendingAggregationRequestList:
    import capo_config_service.types.pending_aggregation_request

    out: PendingAggregationRequestList = []
    for item in data:
        out.append(
            capo_config_service.types.pending_aggregation_request.deserialize_aws_json_1_1(
                item
            )
        )
    return out
