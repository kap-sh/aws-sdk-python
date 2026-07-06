"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#GetReadinessCheckStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__string
    import aws_sdk_route53_recovery_readiness.types.max_results


class GetReadinessCheckStatusRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.max_results.MaxResults"
    ]
    """<p>The number of objects that you want to return with this call.</p>"""
    next_token: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    readiness_check_name: "aws_sdk_route53_recovery_readiness.types.__string.__string"
    """<p>Name of a readiness check.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReadinessCheckStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReadinessCheckStatusRequest:
    out: GetReadinessCheckStatusRequest = {}  # type: ignore[typeddict-item]
    return out
