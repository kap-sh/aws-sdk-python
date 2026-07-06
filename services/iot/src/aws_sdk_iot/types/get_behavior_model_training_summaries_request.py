"""Generated from Smithy shape ``com.amazonaws.iot#GetBehaviorModelTrainingSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.security_profile_name
    import aws_sdk_iot.types.tiny_max_results


class GetBehaviorModelTrainingSummariesRequest(TypedDict, closed=True):
    security_profile_name: NotRequired[
        "aws_sdk_iot.types.security_profile_name.SecurityProfileName"
    ]
    """<p> The name of the security profile. </p>"""
    max_results: NotRequired["aws_sdk_iot.types.tiny_max_results.TinyMaxResults"]
    """<p> The maximum number of results to return at one time. The default is 10. </p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p> The token for the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBehaviorModelTrainingSummariesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBehaviorModelTrainingSummariesRequest:
    out: GetBehaviorModelTrainingSummariesRequest = {}  # type: ignore[typeddict-item]
    return out
