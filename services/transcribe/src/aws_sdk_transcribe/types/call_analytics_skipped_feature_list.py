"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsSkippedFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.call_analytics_skipped_feature

CallAnalyticsSkippedFeatureList: TypeAlias = list[
    "aws_sdk_transcribe.types.call_analytics_skipped_feature.CallAnalyticsSkippedFeature"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallAnalyticsSkippedFeatureList) -> list:
    import aws_sdk_transcribe.types.call_analytics_skipped_feature

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transcribe.types.call_analytics_skipped_feature.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CallAnalyticsSkippedFeatureList:
    import aws_sdk_transcribe.types.call_analytics_skipped_feature

    out: CallAnalyticsSkippedFeatureList = []
    for item in data:
        out.append(
            aws_sdk_transcribe.types.call_analytics_skipped_feature.deserialize_aws_json_1_1(
                item
            )
        )
    return out
