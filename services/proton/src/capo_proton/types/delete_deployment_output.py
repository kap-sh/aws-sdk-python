"""Generated from Smithy shape ``com.amazonaws.proton#DeleteDeploymentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.deployment


class DeleteDeploymentOutput(TypedDict, closed=True):
    deployment: NotRequired["capo_proton.types.deployment.Deployment"]
    """<p>The detailed data of the deployment being deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDeploymentOutput) -> dict:
    out: dict = {}
    if "deployment" in value:
        import capo_proton.types.deployment

        out["deployment"] = capo_proton.types.deployment.serialize_aws_json_1_0(
            value["deployment"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDeploymentOutput:
    out: DeleteDeploymentOutput = {}  # type: ignore[typeddict-item]
    if "deployment" in data:
        import capo_proton.types.deployment

        out["deployment"] = capo_proton.types.deployment.deserialize_aws_json_1_0(
            data["deployment"]
        )
    return out
