"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#ListClustersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__string
    import capo_route53_recovery_control_config.types.max_results


class ListClustersRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_route53_recovery_control_config.types.max_results.MaxResults"
    ]
    """<p>The number of objects that you want to return with this call.</p>"""
    next_token: NotRequired[
        "capo_route53_recovery_control_config.types.__string.__string"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClustersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListClustersRequest:
    out: ListClustersRequest = {}  # type: ignore[typeddict-item]
    return out
