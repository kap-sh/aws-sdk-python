"""Generated from Smithy shape ``com.amazonaws.appconfig#GetDeploymentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.integer


class GetDeploymentRequest(TypedDict):
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The ID of the application that includes the deployment you want to get. </p>"""
    environment_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The ID of the environment that includes the deployment you want to get. </p>"""
    deployment_number: "aws_sdk_appconfig.types.integer.Integer"
    """<p>The sequence number of the deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDeploymentRequest:
    out: GetDeploymentRequest = {}  # type: ignore[typeddict-item]
    return out
