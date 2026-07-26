"""Generated from Smithy shape ``com.amazonaws.qbusiness#OrchestrationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.orchestration_control


class OrchestrationConfiguration(TypedDict, closed=True):
    control: "capo_qbusiness.types.orchestration_control.OrchestrationControl"
    """<p> Status information about whether chat orchestration is activated or deactivated for your Amazon Q Business application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrchestrationConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.orchestration_control

    out["control"] = capo_qbusiness.types.orchestration_control.serialize_json(
        value["control"]
    )
    return out


def deserialize_json(data: dict) -> OrchestrationConfiguration:
    out: OrchestrationConfiguration = {}  # type: ignore[typeddict-item]
    if "control" in data:
        import capo_qbusiness.types.orchestration_control

        out["control"] = capo_qbusiness.types.orchestration_control.deserialize_json(
            data["control"]
        )
    else:
        raise DeserializationError("OrchestrationConfiguration.control required")
    return out
