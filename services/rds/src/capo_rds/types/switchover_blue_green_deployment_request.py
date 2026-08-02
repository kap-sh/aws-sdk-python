"""Generated from Smithy shape ``com.amazonaws.rds#SwitchoverBlueGreenDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.blue_green_deployment_identifier
    import capo_rds.types.switchover_timeout


class SwitchoverBlueGreenDeploymentRequest(TypedDict, closed=True):
    blue_green_deployment_identifier: NotRequired[
        "capo_rds.types.blue_green_deployment_identifier.BlueGreenDeploymentIdentifier"
    ]
    """<p>The resource ID of the blue/green deployment.</p> <p>Constraints:</p> <ul> <li> <p>Must match an existing blue/green deployment resource ID.</p> </li> </ul>"""
    switchover_timeout: NotRequired[
        "capo_rds.types.switchover_timeout.SwitchoverTimeout"
    ]
    """<p>The amount of time, in seconds, for the switchover to complete.</p> <p>Default: 300</p> <p>If the switchover takes longer than the specified duration, then any changes are rolled back, and no changes are made to the environments.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SwitchoverBlueGreenDeploymentRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "blue_green_deployment_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}BlueGreenDeploymentIdentifier",
                str(value["blue_green_deployment_identifier"]),
            )
        )
    if "switchover_timeout" in value:
        pairs.append(
            (f"{key_prefix}SwitchoverTimeout", str(value["switchover_timeout"]))
        )


def deserialize_query(el: Element) -> SwitchoverBlueGreenDeploymentRequest:
    out: SwitchoverBlueGreenDeploymentRequest = {}  # type: ignore[typeddict-item]
    child_blue_green_deployment_identifier = el.find("BlueGreenDeploymentIdentifier")
    if child_blue_green_deployment_identifier is not None:
        out["blue_green_deployment_identifier"] = str(
            child_blue_green_deployment_identifier.text or ""
        )
    child_switchover_timeout = el.find("SwitchoverTimeout")
    if child_switchover_timeout is not None:
        out["switchover_timeout"] = int(child_switchover_timeout.text or "")
    return out
