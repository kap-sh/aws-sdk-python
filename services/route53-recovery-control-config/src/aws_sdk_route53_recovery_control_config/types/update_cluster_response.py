"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#UpdateClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.cluster


class UpdateClusterResponse(TypedDict, closed=True):
    cluster: NotRequired[
        "aws_sdk_route53_recovery_control_config.types.cluster.Cluster"
    ]
    """<p>The cluster that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import aws_sdk_route53_recovery_control_config.types.cluster

        out["Cluster"] = (
            aws_sdk_route53_recovery_control_config.types.cluster.serialize_json(
                value["cluster"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateClusterResponse:
    out: UpdateClusterResponse = {}  # type: ignore[typeddict-item]
    if "Cluster" in data:
        import aws_sdk_route53_recovery_control_config.types.cluster

        out["cluster"] = (
            aws_sdk_route53_recovery_control_config.types.cluster.deserialize_json(
                data["Cluster"]
            )
        )
    return out
