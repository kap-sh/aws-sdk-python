"""Generated from Smithy shape ``com.amazonaws.proton#CancelComponentDeploymentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.component


class CancelComponentDeploymentOutput(TypedDict, closed=True):
    component: "capo_proton.types.component.Component"
    """<p>The detailed data of the component with the deployment that is being canceled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelComponentDeploymentOutput) -> dict:
    out: dict = {}
    import capo_proton.types.component

    out["component"] = capo_proton.types.component.serialize_aws_json_1_0(
        value["component"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelComponentDeploymentOutput:
    out: CancelComponentDeploymentOutput = {}  # type: ignore[typeddict-item]
    if "component" in data:
        import capo_proton.types.component

        out["component"] = capo_proton.types.component.deserialize_aws_json_1_0(
            data["component"]
        )
    else:
        raise DeserializationError("CancelComponentDeploymentOutput.component required")
    return out
