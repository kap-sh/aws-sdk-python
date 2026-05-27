"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentEphemeralStorage``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DeploymentEphemeralStorage(TypedDict):
    kms_key_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Specify an Key Management Service key ID to encrypt the ephemeral storage for deployment.</p>"""
