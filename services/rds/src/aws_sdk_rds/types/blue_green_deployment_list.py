"""Generated from Smithy shape ``com.amazonaws.rds#BlueGreenDeploymentList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.blue_green_deployment

BlueGreenDeploymentList: TypeAlias = list[
    "aws_sdk_rds.types.blue_green_deployment.BlueGreenDeployment"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: BlueGreenDeploymentList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.blue_green_deployment

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.blue_green_deployment.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> BlueGreenDeploymentList:
    import aws_sdk_rds.types.blue_green_deployment

    out: BlueGreenDeploymentList = []
    for child in el.findall("member"):
        out.append(aws_sdk_rds.types.blue_green_deployment.deserialize_query(child))
    return out


def serialize_query_flat(
    value: BlueGreenDeploymentList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.blue_green_deployment

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.blue_green_deployment.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> BlueGreenDeploymentList:
    import aws_sdk_rds.types.blue_green_deployment

    out: BlueGreenDeploymentList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.blue_green_deployment.deserialize_query(child))
    return out
