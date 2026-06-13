"""Generated from Smithy shape ``com.amazonaws.qconnect#NotifyRecommendationsReceivedErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.notify_recommendations_received_error

NotifyRecommendationsReceivedErrorList: TypeAlias = list[
    "aws_sdk_qconnect.types.notify_recommendations_received_error.NotifyRecommendationsReceivedError"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotifyRecommendationsReceivedErrorList) -> list:
    import aws_sdk_qconnect.types.notify_recommendations_received_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qconnect.types.notify_recommendations_received_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NotifyRecommendationsReceivedErrorList:
    import aws_sdk_qconnect.types.notify_recommendations_received_error

    out: NotifyRecommendationsReceivedErrorList = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.notify_recommendations_received_error.deserialize_json(
                item
            )
        )
    return out
