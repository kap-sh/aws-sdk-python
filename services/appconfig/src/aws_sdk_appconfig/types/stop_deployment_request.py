"""Generated from Smithy shape ``com.amazonaws.appconfig#StopDeploymentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.boolean
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.integer


class StopDeploymentRequest(TypedDict):
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The application ID.</p>"""
    environment_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The environment ID.</p>"""
    deployment_number: "aws_sdk_appconfig.types.integer.Integer"
    """<p>The sequence number of the deployment.</p>"""
    allow_revert: NotRequired["aws_sdk_appconfig.types.boolean.Boolean"]
    """<p>A Boolean that enables AppConfig to rollback a <code>COMPLETED</code> deployment to the previous configuration version. This action moves the deployment to a status of <code>REVERTED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopDeploymentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopDeploymentRequest:
    out: StopDeploymentRequest = {}  # type: ignore[typeddict-item]
    return out
