"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#ListAssociatedRoute53HealthChecksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.__string
    import aws_sdk_route53_recovery_control_config.types.max_results


class ListAssociatedRoute53HealthChecksRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.max_results.MaxResults"
    ]
    """<p>The number of objects that you want to return with this call.</p>"""
    next_token: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.__string.__string"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    routing_control_arn: (
        "aws_sdk_route53_recovery_control_config.types.__string.__string"
    )
    """<p>The Amazon Resource Name (ARN) of the routing control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedRoute53HealthChecksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssociatedRoute53HealthChecksRequest:
    out: ListAssociatedRoute53HealthChecksRequest = {}  # type: ignore[typeddict-item]
    return out
