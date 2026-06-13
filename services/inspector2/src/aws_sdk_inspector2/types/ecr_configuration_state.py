"""Generated from Smithy shape ``com.amazonaws.inspector2#EcrConfigurationState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.ecr_rescan_duration_state


class EcrConfigurationState(TypedDict):
    rescan_duration_state: NotRequired[
        "aws_sdk_inspector2.types.ecr_rescan_duration_state.EcrRescanDurationState"
    ]
    """<p>An object that contains details about the state of the ECR re-scan settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcrConfigurationState) -> dict:
    out: dict = {}
    if "rescan_duration_state" in value:
        import aws_sdk_inspector2.types.ecr_rescan_duration_state

        out["rescanDurationState"] = (
            aws_sdk_inspector2.types.ecr_rescan_duration_state.serialize_json(
                value["rescan_duration_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> EcrConfigurationState:
    out: EcrConfigurationState = {}  # type: ignore[typeddict-item]
    if "rescanDurationState" in data:
        import aws_sdk_inspector2.types.ecr_rescan_duration_state

        out["rescan_duration_state"] = (
            aws_sdk_inspector2.types.ecr_rescan_duration_state.deserialize_json(
                data["rescanDurationState"]
            )
        )
    return out
