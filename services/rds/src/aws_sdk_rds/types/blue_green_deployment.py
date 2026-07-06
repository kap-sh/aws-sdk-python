"""Generated from Smithy shape ``com.amazonaws.rds#BlueGreenDeployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.blue_green_deployment_identifier
    import aws_sdk_rds.types.blue_green_deployment_name
    import aws_sdk_rds.types.blue_green_deployment_status
    import aws_sdk_rds.types.blue_green_deployment_status_details
    import aws_sdk_rds.types.blue_green_deployment_task_list
    import aws_sdk_rds.types.database_arn
    import aws_sdk_rds.types.switchover_detail_list
    import aws_sdk_rds.types.t_stamp
    import aws_sdk_rds.types.tag_list


class BlueGreenDeployment(TypedDict, closed=True):
    blue_green_deployment_identifier: NotRequired[
        "aws_sdk_rds.types.blue_green_deployment_identifier.BlueGreenDeploymentIdentifier"
    ]
    """<p>The unique identifier of the blue/green deployment.</p>"""
    blue_green_deployment_name: NotRequired[
        "aws_sdk_rds.types.blue_green_deployment_name.BlueGreenDeploymentName"
    ]
    """<p>The user-supplied name of the blue/green deployment.</p>"""
    source: NotRequired["aws_sdk_rds.types.database_arn.DatabaseArn"]
    """<p>The source database for the blue/green deployment.</p> <p>Before switchover, the source database is the production database in the blue environment.</p>"""
    target: NotRequired["aws_sdk_rds.types.database_arn.DatabaseArn"]
    """<p>The target database for the blue/green deployment.</p> <p>Before switchover, the target database is the clone database in the green environment.</p>"""
    switchover_details: NotRequired[
        "aws_sdk_rds.types.switchover_detail_list.SwitchoverDetailList"
    ]
    """<p>The details about each source and target resource in the blue/green deployment.</p>"""
    tasks: NotRequired[
        "aws_sdk_rds.types.blue_green_deployment_task_list.BlueGreenDeploymentTaskList"
    ]
    """<p>Either tasks to be performed or tasks that have been completed on the target database before switchover.</p>"""
    status: NotRequired[
        "aws_sdk_rds.types.blue_green_deployment_status.BlueGreenDeploymentStatus"
    ]
    """<p>The status of the blue/green deployment.</p> <p>Valid Values:</p> <ul> <li> <p> <code>PROVISIONING</code> - Resources are being created in the green environment.</p> </li> <li> <p> <code>AVAILABLE</code> - Resources are available in the green environment.</p> </li> <li> <p> <code>SWITCHOVER_IN_PROGRESS</code> - The deployment is being switched from the blue environment to the green environment.</p> </li> <li> <p> <code>SWITCHOVER_COMPLETED</code> - Switchover from the blue environment to the green environment is complete.</p> </li> <li> <p> <code>INVALID_CONFIGURATION</code> - Resources in the green environment are invalid, so switchover isn't possible.</p> </li> <li> <p> <code>SWITCHOVER_FAILED</code> - Switchover was attempted but failed.</p> </li> <li> <p> <code>DELETING</code> - The blue/green deployment is being deleted.</p> </li> </ul>"""
    status_details: NotRequired[
        "aws_sdk_rds.types.blue_green_deployment_status_details.BlueGreenDeploymentStatusDetails"
    ]
    """<p>Additional information about the status of the blue/green deployment.</p>"""
    create_time: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The time when the blue/green deployment was created, in Universal Coordinated Time (UTC).</p>"""
    delete_time: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The time when the blue/green deployment was deleted, in Universal Coordinated Time (UTC).</p>"""
    tag_list: NotRequired["aws_sdk_rds.types.tag_list.TagList"]


# --- awsQuery ser/de ---
def serialize_query(
    value: BlueGreenDeployment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "blue_green_deployment_identifier" in value:
        pairs.append(
            (
                f"{prefix}.BlueGreenDeploymentIdentifier",
                str(value["blue_green_deployment_identifier"]),
            )
        )
    if "blue_green_deployment_name" in value:
        pairs.append(
            (
                f"{prefix}.BlueGreenDeploymentName",
                str(value["blue_green_deployment_name"]),
            )
        )
    if "source" in value:
        pairs.append((f"{prefix}.Source", str(value["source"])))
    if "target" in value:
        pairs.append((f"{prefix}.Target", str(value["target"])))
    if "switchover_details" in value:
        import aws_sdk_rds.types.switchover_detail_list

        aws_sdk_rds.types.switchover_detail_list.serialize_query(
            value["switchover_details"], pairs, f"{prefix}.SwitchoverDetails"
        )
    if "tasks" in value:
        import aws_sdk_rds.types.blue_green_deployment_task_list

        aws_sdk_rds.types.blue_green_deployment_task_list.serialize_query(
            value["tasks"], pairs, f"{prefix}.Tasks"
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "status_details" in value:
        pairs.append((f"{prefix}.StatusDetails", str(value["status_details"])))
    if "create_time" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["create_time"], pairs, f"{prefix}.CreateTime"
        )
    if "delete_time" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["delete_time"], pairs, f"{prefix}.DeleteTime"
        )
    if "tag_list" in value:
        import aws_sdk_rds.types.tag_list

        aws_sdk_rds.types.tag_list.serialize_query(
            value["tag_list"], pairs, f"{prefix}.TagList"
        )


def deserialize_query(el: Element) -> BlueGreenDeployment:
    out: BlueGreenDeployment = {}  # type: ignore[typeddict-item]
    child_blue_green_deployment_identifier = el.find("BlueGreenDeploymentIdentifier")
    if child_blue_green_deployment_identifier is not None:
        out["blue_green_deployment_identifier"] = str(
            child_blue_green_deployment_identifier.text or ""
        )
    child_blue_green_deployment_name = el.find("BlueGreenDeploymentName")
    if child_blue_green_deployment_name is not None:
        out["blue_green_deployment_name"] = str(
            child_blue_green_deployment_name.text or ""
        )
    child_source = el.find("Source")
    if child_source is not None:
        out["source"] = str(child_source.text or "")
    child_target = el.find("Target")
    if child_target is not None:
        out["target"] = str(child_target.text or "")
    child_switchover_details = el.find("SwitchoverDetails")
    if child_switchover_details is not None:
        import aws_sdk_rds.types.switchover_detail_list

        out["switchover_details"] = (
            aws_sdk_rds.types.switchover_detail_list.deserialize_query(
                child_switchover_details
            )
        )
    child_tasks = el.find("Tasks")
    if child_tasks is not None:
        import aws_sdk_rds.types.blue_green_deployment_task_list

        out["tasks"] = (
            aws_sdk_rds.types.blue_green_deployment_task_list.deserialize_query(
                child_tasks
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_status_details = el.find("StatusDetails")
    if child_status_details is not None:
        out["status_details"] = str(child_status_details.text or "")
    child_create_time = el.find("CreateTime")
    if child_create_time is not None:
        import aws_sdk_rds.types.t_stamp

        out["create_time"] = aws_sdk_rds.types.t_stamp.deserialize_query(
            child_create_time
        )
    child_delete_time = el.find("DeleteTime")
    if child_delete_time is not None:
        import aws_sdk_rds.types.t_stamp

        out["delete_time"] = aws_sdk_rds.types.t_stamp.deserialize_query(
            child_delete_time
        )
    child_tag_list = el.find("TagList")
    if child_tag_list is not None:
        import aws_sdk_rds.types.tag_list

        out["tag_list"] = aws_sdk_rds.types.tag_list.deserialize_query(child_tag_list)
    return out
