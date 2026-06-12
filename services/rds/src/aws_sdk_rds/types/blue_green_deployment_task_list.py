"""Generated from Smithy shape ``com.amazonaws.rds#BlueGreenDeploymentTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.blue_green_deployment_task

BlueGreenDeploymentTaskList: TypeAlias = list[
    "aws_sdk_rds.types.blue_green_deployment_task.BlueGreenDeploymentTask"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: BlueGreenDeploymentTaskList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.blue_green_deployment_task

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.blue_green_deployment_task.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> BlueGreenDeploymentTaskList:
    import aws_sdk_rds.types.blue_green_deployment_task

    out: BlueGreenDeploymentTaskList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_rds.types.blue_green_deployment_task.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: BlueGreenDeploymentTaskList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.blue_green_deployment_task

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.blue_green_deployment_task.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> BlueGreenDeploymentTaskList:
    import aws_sdk_rds.types.blue_green_deployment_task

    out: BlueGreenDeploymentTaskList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_rds.types.blue_green_deployment_task.deserialize_query(child)
        )
    return out
