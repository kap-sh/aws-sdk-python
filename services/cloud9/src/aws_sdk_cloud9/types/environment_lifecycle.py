"""Generated from Smithy shape ``com.amazonaws.cloud9#EnvironmentLifecycle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.environment_lifecycle_status
    import aws_sdk_cloud9.types.string


class EnvironmentLifecycle(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_cloud9.types.environment_lifecycle_status.EnvironmentLifecycleStatus"
    ]
    """<p>The current creation or deletion lifecycle state of the environment.</p> <ul> <li> <p> <code>CREATING</code>: The environment is in the process of being created.</p> </li> <li> <p> <code>CREATED</code>: The environment was successfully created.</p> </li> <li> <p> <code>CREATE_FAILED</code>: The environment failed to be created.</p> </li> <li> <p> <code>DELETING</code>: The environment is in the process of being deleted.</p> </li> <li> <p> <code>DELETE_FAILED</code>: The environment failed to delete.</p> </li> </ul>"""
    reason: NotRequired["aws_sdk_cloud9.types.string.String"]
    """<p>Any informational message about the lifecycle state of the environment.</p>"""
    failure_resource: NotRequired["aws_sdk_cloud9.types.string.String"]
    """<p>If the environment failed to delete, the Amazon Resource Name (ARN) of the related Amazon Web Services resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentLifecycle) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_cloud9.types.environment_lifecycle_status

        out["status"] = (
            aws_sdk_cloud9.types.environment_lifecycle_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    if "failure_resource" in value:
        out["failureResource"] = value["failure_resource"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentLifecycle:
    out: EnvironmentLifecycle = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_cloud9.types.environment_lifecycle_status

        out["status"] = (
            aws_sdk_cloud9.types.environment_lifecycle_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    if "failureResource" in data:
        out["failure_resource"] = data["failureResource"]
    return out
