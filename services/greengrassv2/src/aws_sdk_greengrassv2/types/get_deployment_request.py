"""Generated from Smithy shape ``com.amazonaws.greengrassv2#GetDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.non_empty_string


class GetDeploymentRequest(TypedDict, closed=True):
    deployment_id: "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString"
    """<p>The ID of the deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDeploymentRequest:
    out: GetDeploymentRequest = {}  # type: ignore[typeddict-item]
    return out
