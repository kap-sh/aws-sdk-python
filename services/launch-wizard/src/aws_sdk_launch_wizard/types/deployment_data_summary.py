"""Generated from Smithy shape ``com.amazonaws.launchwizard#DeploymentDataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_launch_wizard.types.deployment_id
    import aws_sdk_launch_wizard.types.deployment_pattern_name
    import aws_sdk_launch_wizard.types.deployment_status
    import aws_sdk_launch_wizard.types.workload_name


class DeploymentDataSummary(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the deployment</p>"""
    id: NotRequired["aws_sdk_launch_wizard.types.deployment_id.DeploymentId"]
    """<p>The ID of the deployment.</p>"""
    workload_name: NotRequired["aws_sdk_launch_wizard.types.workload_name.WorkloadName"]
    """<p>The name of the workload.</p>"""
    pattern_name: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_pattern_name.DeploymentPatternName"
    ]
    """<p>The name of the workload deployment pattern.</p>"""
    status: NotRequired[
        "aws_sdk_launch_wizard.types.deployment_status.DeploymentStatus"
    ]
    """<p>The status of the deployment.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time the deployment was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p>The time the deployment was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentDataSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "workload_name" in value:
        out["workloadName"] = value["workload_name"]
    if "pattern_name" in value:
        out["patternName"] = value["pattern_name"]
    if "status" in value:
        import aws_sdk_launch_wizard.types.deployment_status

        out["status"] = aws_sdk_launch_wizard.types.deployment_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import aws_sdk_launch_wizard.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_launch_wizard.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "modified_at" in value:
        import aws_sdk_launch_wizard.types._prelude.timestamp

        out["modifiedAt"] = (
            aws_sdk_launch_wizard.types._prelude.timestamp.serialize_json(
                value["modified_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeploymentDataSummary:
    out: DeploymentDataSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "id" in data:
        out["id"] = data["id"]
    if "workloadName" in data:
        out["workload_name"] = data["workloadName"]
    if "patternName" in data:
        out["pattern_name"] = data["patternName"]
    if "status" in data:
        import aws_sdk_launch_wizard.types.deployment_status

        out["status"] = aws_sdk_launch_wizard.types.deployment_status.deserialize_json(
            data["status"]
        )
    if "createdAt" in data:
        import aws_sdk_launch_wizard.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_launch_wizard.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "modifiedAt" in data:
        import aws_sdk_launch_wizard.types._prelude.timestamp

        out["modified_at"] = (
            aws_sdk_launch_wizard.types._prelude.timestamp.deserialize_json(
                data["modifiedAt"]
            )
        )
    return out
