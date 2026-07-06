"""Generated from Smithy shape ``com.amazonaws.rds#BlueGreenDeploymentTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.blue_green_deployment_task_name
    import aws_sdk_rds.types.blue_green_deployment_task_status


class BlueGreenDeploymentTask(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_rds.types.blue_green_deployment_task_name.BlueGreenDeploymentTaskName"
    ]
    """<p>The name of the blue/green deployment task.</p>"""
    status: NotRequired[
        "aws_sdk_rds.types.blue_green_deployment_task_status.BlueGreenDeploymentTaskStatus"
    ]
    """<p>The status of the blue/green deployment task.</p> <p>Valid Values:</p> <ul> <li> <p> <code>PENDING</code> - The resource is being prepared for deployment.</p> </li> <li> <p> <code>IN_PROGRESS</code> - The resource is being deployed.</p> </li> <li> <p> <code>COMPLETED</code> - The resource has been deployed.</p> </li> <li> <p> <code>FAILED</code> - Deployment of the resource failed.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BlueGreenDeploymentTask, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_query(el: Element) -> BlueGreenDeploymentTask:
    out: BlueGreenDeploymentTask = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
