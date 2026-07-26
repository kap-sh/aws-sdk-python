"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#DeleteClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.__string


class DeleteClusterRequest(TypedDict, closed=True):
    cluster_arn: "capo_route53_recovery_control_config.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the cluster that you're deleting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteClusterRequest:
    out: DeleteClusterRequest = {}  # type: ignore[typeddict-item]
    return out
