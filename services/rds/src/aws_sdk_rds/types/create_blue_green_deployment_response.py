"""Generated from Smithy shape ``com.amazonaws.rds#CreateBlueGreenDeploymentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.blue_green_deployment


class CreateBlueGreenDeploymentResponse(TypedDict):
    blue_green_deployment: NotRequired[
        "aws_sdk_rds.types.blue_green_deployment.BlueGreenDeployment"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateBlueGreenDeploymentResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "blue_green_deployment" in value:
        import aws_sdk_rds.types.blue_green_deployment

        aws_sdk_rds.types.blue_green_deployment.serialize_query(
            value["blue_green_deployment"], pairs, f"{prefix}.BlueGreenDeployment"
        )


def deserialize_query(el: Element) -> CreateBlueGreenDeploymentResponse:
    out: CreateBlueGreenDeploymentResponse = {}  # type: ignore[typeddict-item]
    child_blue_green_deployment = el.find("BlueGreenDeployment")
    if child_blue_green_deployment is not None:
        import aws_sdk_rds.types.blue_green_deployment

        out["blue_green_deployment"] = (
            aws_sdk_rds.types.blue_green_deployment.deserialize_query(
                child_blue_green_deployment
            )
        )
    return out
