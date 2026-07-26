"""Generated from Smithy shape ``com.amazonaws.backup#DescribeFrameworkOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.framework_controls
    import capo_backup.types.framework_description
    import capo_backup.types.framework_name
    import capo_backup.types.string
    import capo_backup.types.timestamp


class DescribeFrameworkOutput(TypedDict, closed=True):
    framework_name: NotRequired["capo_backup.types.framework_name.FrameworkName"]
    """<p>The unique name of a framework.</p>"""
    framework_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>"""
    framework_description: NotRequired[
        "capo_backup.types.framework_description.FrameworkDescription"
    ]
    """<p>An optional description of the framework.</p>"""
    framework_controls: NotRequired[
        "capo_backup.types.framework_controls.FrameworkControls"
    ]
    """<p>The controls that make up the framework. Each control in the list has a name, input parameters, and scope.</p>"""
    creation_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a framework is created, in ISO 8601 representation. The value of <code>CreationTime</code> is accurate to milliseconds. For example, 2020-07-10T15:00:00.000-08:00 represents the 10th of July 2020 at 3:00 PM 8 hours behind UTC.</p>"""
    deployment_status: NotRequired["capo_backup.types.string.string"]
    """<p>The deployment status of a framework. The statuses are:</p> <p> <code>CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | COMPLETED | FAILED</code> </p>"""
    framework_status: NotRequired["capo_backup.types.string.string"]
    """<p>A framework consists of one or more controls. Each control governs a resource, such as backup plans, backup selections, backup vaults, or recovery points. You can also turn Config recording on or off for each resource. The statuses are:</p> <ul> <li> <p> <code>ACTIVE</code> when recording is turned on for all resources governed by the framework.</p> </li> <li> <p> <code>PARTIALLY_ACTIVE</code> when recording is turned off for at least one resource governed by the framework.</p> </li> <li> <p> <code>INACTIVE</code> when recording is turned off for all resources governed by the framework.</p> </li> <li> <p> <code>UNAVAILABLE</code> when Backup is unable to validate recording status at this time.</p> </li> </ul>"""
    idempotency_token: NotRequired["capo_backup.types.string.string"]
    """<p>A customer-chosen string that you can use to distinguish between otherwise identical calls to <code>DescribeFrameworkOutput</code>. Retrying a successful request with the same idempotency token results in a success message with no action taken.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFrameworkOutput) -> dict:
    out: dict = {}
    if "framework_name" in value:
        out["FrameworkName"] = value["framework_name"]
    if "framework_arn" in value:
        out["FrameworkArn"] = value["framework_arn"]
    if "framework_description" in value:
        out["FrameworkDescription"] = value["framework_description"]
    if "framework_controls" in value:
        import capo_backup.types.framework_controls

        out["FrameworkControls"] = capo_backup.types.framework_controls.serialize_json(
            value["framework_controls"]
        )
    if "creation_time" in value:
        import capo_backup.types.timestamp

        out["CreationTime"] = capo_backup.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "deployment_status" in value:
        out["DeploymentStatus"] = value["deployment_status"]
    if "framework_status" in value:
        out["FrameworkStatus"] = value["framework_status"]
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_json(data: dict) -> DescribeFrameworkOutput:
    out: DescribeFrameworkOutput = {}  # type: ignore[typeddict-item]
    if "FrameworkName" in data:
        out["framework_name"] = data["FrameworkName"]
    if "FrameworkArn" in data:
        out["framework_arn"] = data["FrameworkArn"]
    if "FrameworkDescription" in data:
        out["framework_description"] = data["FrameworkDescription"]
    if "FrameworkControls" in data:
        import capo_backup.types.framework_controls

        out["framework_controls"] = (
            capo_backup.types.framework_controls.deserialize_json(
                data["FrameworkControls"]
            )
        )
    if "CreationTime" in data:
        import capo_backup.types.timestamp

        out["creation_time"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "DeploymentStatus" in data:
        out["deployment_status"] = data["DeploymentStatus"]
    if "FrameworkStatus" in data:
        out["framework_status"] = data["FrameworkStatus"]
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
