"""Generated from Smithy shape ``com.amazonaws.iot#VersionUpdateByJobsConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.enabled_boolean
    import capo_iot.types.role_arn


class VersionUpdateByJobsConfig(TypedDict, closed=True):
    enabled: NotRequired["capo_iot.types.enabled_boolean.EnabledBoolean"]
    """<p>Indicates whether the Job is enabled or not.</p>"""
    role_arn: NotRequired["capo_iot.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role that grants permission to the IoT jobs service to update the reserved named shadow when the job successfully completes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VersionUpdateByJobsConfig) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> VersionUpdateByJobsConfig:
    out: VersionUpdateByJobsConfig = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out
