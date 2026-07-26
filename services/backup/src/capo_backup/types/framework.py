"""Generated from Smithy shape ``com.amazonaws.backup#Framework``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.framework_description
    import capo_backup.types.framework_name
    import capo_backup.types.integer
    import capo_backup.types.string
    import capo_backup.types.timestamp


class Framework(TypedDict, closed=True):
    framework_name: NotRequired["capo_backup.types.framework_name.FrameworkName"]
    """<p>The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</p>"""
    framework_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>"""
    framework_description: NotRequired[
        "capo_backup.types.framework_description.FrameworkDescription"
    ]
    """<p>An optional description of the framework with a maximum 1,024 characters.</p>"""
    number_of_controls: "capo_backup.types.integer.integer"
    """<p>The number of controls contained by the framework.</p>"""
    creation_time: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The date and time that a framework is created, in ISO 8601 representation. The value of <code>CreationTime</code> is accurate to milliseconds. For example, 2020-07-10T15:00:00.000-08:00 represents the 10th of July 2020 at 3:00 PM 8 hours behind UTC.</p>"""
    deployment_status: NotRequired["capo_backup.types.string.string"]
    """<p>The deployment status of a framework. The statuses are:</p> <p> <code>CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | COMPLETED | FAILED</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Framework) -> dict:
    out: dict = {}
    if "framework_name" in value:
        out["FrameworkName"] = value["framework_name"]
    if "framework_arn" in value:
        out["FrameworkArn"] = value["framework_arn"]
    if "framework_description" in value:
        out["FrameworkDescription"] = value["framework_description"]
    out["NumberOfControls"] = value.get("number_of_controls", 0)
    if "creation_time" in value:
        import capo_backup.types.timestamp

        out["CreationTime"] = capo_backup.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "deployment_status" in value:
        out["DeploymentStatus"] = value["deployment_status"]
    return out


def deserialize_json(data: dict) -> Framework:
    out: Framework = {}  # type: ignore[typeddict-item]
    if "FrameworkName" in data:
        out["framework_name"] = data["FrameworkName"]
    if "FrameworkArn" in data:
        out["framework_arn"] = data["FrameworkArn"]
    if "FrameworkDescription" in data:
        out["framework_description"] = data["FrameworkDescription"]
    if "NumberOfControls" in data:
        out["number_of_controls"] = data["NumberOfControls"]
    else:
        out["number_of_controls"] = 0
    if "CreationTime" in data:
        import capo_backup.types.timestamp

        out["creation_time"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "DeploymentStatus" in data:
        out["deployment_status"] = data["DeploymentStatus"]
    return out
