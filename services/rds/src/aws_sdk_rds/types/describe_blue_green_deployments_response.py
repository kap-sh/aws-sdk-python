"""Generated from Smithy shape ``com.amazonaws.rds#DescribeBlueGreenDeploymentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.blue_green_deployment_list
    import aws_sdk_rds.types.string


class DescribeBlueGreenDeploymentsResponse(TypedDict):
    blue_green_deployments: NotRequired[
        "aws_sdk_rds.types.blue_green_deployment_list.BlueGreenDeploymentList"
    ]
    """<p>A list of blue/green deployments in the current account and Amazon Web Services Region.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A pagination token that can be used in a later <code>DescribeBlueGreenDeployments</code> request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeBlueGreenDeploymentsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "blue_green_deployments" in value:
        import aws_sdk_rds.types.blue_green_deployment_list

        aws_sdk_rds.types.blue_green_deployment_list.serialize_query(
            value["blue_green_deployments"], pairs, f"{prefix}.BlueGreenDeployments"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeBlueGreenDeploymentsResponse:
    out: DescribeBlueGreenDeploymentsResponse = {}  # type: ignore[typeddict-item]
    child_blue_green_deployments = el.find("BlueGreenDeployments")
    if child_blue_green_deployments is not None:
        import aws_sdk_rds.types.blue_green_deployment_list

        out["blue_green_deployments"] = (
            aws_sdk_rds.types.blue_green_deployment_list.deserialize_query(
                child_blue_green_deployments
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
