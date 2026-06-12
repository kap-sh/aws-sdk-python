"""Generated from Smithy shape ``com.amazonaws.m2#DeployedVersionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.deployment_lifecycle
    import aws_sdk_m2.types.version


class DeployedVersionSummary(TypedDict):
    application_version: "aws_sdk_m2.types.version.Version"
    """<p>The version of the deployed application.</p>"""
    status: "aws_sdk_m2.types.deployment_lifecycle.DeploymentLifecycle"
    """<p>The status of the deployment.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the reported status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeployedVersionSummary) -> dict:
    out: dict = {}
    out["applicationVersion"] = value["application_version"]
    out["status"] = value["status"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> DeployedVersionSummary:
    out: DeployedVersionSummary = {}  # type: ignore[typeddict-item]
    if "applicationVersion" in data:
        out["application_version"] = data["applicationVersion"]
    else:
        raise DeserializationError(
            "DeployedVersionSummary.application_version required"
        )
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("DeployedVersionSummary.status required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
