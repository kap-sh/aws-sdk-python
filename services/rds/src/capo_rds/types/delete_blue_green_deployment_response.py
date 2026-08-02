"""Generated from Smithy shape ``com.amazonaws.rds#DeleteBlueGreenDeploymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.blue_green_deployment


class DeleteBlueGreenDeploymentResponse(TypedDict, closed=True):
    blue_green_deployment: NotRequired[
        "capo_rds.types.blue_green_deployment.BlueGreenDeployment"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteBlueGreenDeploymentResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "blue_green_deployment" in value:
        import capo_rds.types.blue_green_deployment

        capo_rds.types.blue_green_deployment.serialize_query(
            value["blue_green_deployment"], pairs, f"{key_prefix}BlueGreenDeployment"
        )


def deserialize_query(el: Element) -> DeleteBlueGreenDeploymentResponse:
    out: DeleteBlueGreenDeploymentResponse = {}  # type: ignore[typeddict-item]
    child_blue_green_deployment = el.find("BlueGreenDeployment")
    if child_blue_green_deployment is not None:
        import capo_rds.types.blue_green_deployment

        out["blue_green_deployment"] = (
            capo_rds.types.blue_green_deployment.deserialize_query(
                child_blue_green_deployment
            )
        )
    return out
