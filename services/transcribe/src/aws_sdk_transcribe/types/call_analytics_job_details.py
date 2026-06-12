"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsJobDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.call_analytics_skipped_feature_list


class CallAnalyticsJobDetails(TypedDict):
    skipped: NotRequired[
        "aws_sdk_transcribe.types.call_analytics_skipped_feature_list.CallAnalyticsSkippedFeatureList"
    ]
    """<p>Contains information about any skipped analytics features during the analysis of a call analytics job.</p> <p>This array lists all the analytics features that were skipped, along with their corresponding reason code and message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallAnalyticsJobDetails) -> dict:
    out: dict = {}
    if "skipped" in value:
        import aws_sdk_transcribe.types.call_analytics_skipped_feature_list

        out["Skipped"] = (
            aws_sdk_transcribe.types.call_analytics_skipped_feature_list.serialize_aws_json_1_1(
                value["skipped"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CallAnalyticsJobDetails:
    out: CallAnalyticsJobDetails = {}  # type: ignore[typeddict-item]
    if "Skipped" in data:
        import aws_sdk_transcribe.types.call_analytics_skipped_feature_list

        out["skipped"] = (
            aws_sdk_transcribe.types.call_analytics_skipped_feature_list.deserialize_aws_json_1_1(
                data["Skipped"]
            )
        )
    return out
