"""Generated from Smithy shape ``com.amazonaws.greengrassv2#CancelDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.non_empty_string


class CancelDeploymentRequest(TypedDict, closed=True):
    deployment_id: "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString"
    """<p>The ID of the deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelDeploymentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelDeploymentRequest:
    out: CancelDeploymentRequest = {}  # type: ignore[typeddict-item]
    return out
