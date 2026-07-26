"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeleteDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.non_empty_string


class DeleteDeploymentRequest(TypedDict, closed=True):
    deployment_id: "capo_greengrassv2.types.non_empty_string.NonEmptyString"
    """<p>The ID of the deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDeploymentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDeploymentRequest:
    out: DeleteDeploymentRequest = {}  # type: ignore[typeddict-item]
    return out
