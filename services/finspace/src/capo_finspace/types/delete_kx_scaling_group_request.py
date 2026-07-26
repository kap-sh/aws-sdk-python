"""Generated from Smithy shape ``com.amazonaws.finspace#DeleteKxScalingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.client_token_string
    import capo_finspace.types.kx_environment_id
    import capo_finspace.types.kx_scaling_group_name


class DeleteKxScalingGroupRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment, from where you want to delete the dataview. </p>"""
    scaling_group_name: "capo_finspace.types.kx_scaling_group_name.KxScalingGroupName"
    """<p>A unique identifier for the kdb scaling group. </p>"""
    client_token: NotRequired[
        "capo_finspace.types.client_token_string.ClientTokenString"
    ]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKxScalingGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteKxScalingGroupRequest:
    out: DeleteKxScalingGroupRequest = {}  # type: ignore[typeddict-item]
    return out
