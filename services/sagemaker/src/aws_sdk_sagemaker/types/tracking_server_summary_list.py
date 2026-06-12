"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrackingServerSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.tracking_server_summary

TrackingServerSummaryList: TypeAlias = list[
    "aws_sdk_sagemaker.types.tracking_server_summary.TrackingServerSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrackingServerSummaryList) -> list:
    import aws_sdk_sagemaker.types.tracking_server_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.tracking_server_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrackingServerSummaryList:
    import aws_sdk_sagemaker.types.tracking_server_summary

    out: TrackingServerSummaryList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.tracking_server_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
