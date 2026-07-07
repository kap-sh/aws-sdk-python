"""Generated from Smithy shape ``com.amazonaws.applicationsignals#GetServiceLevelObjectiveOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.service_level_objective


class GetServiceLevelObjectiveOutput(TypedDict, closed=True):
    slo: "aws_sdk_application_signals.types.service_level_objective.ServiceLevelObjective"
    """<p>A structure containing the information about the SLO.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceLevelObjectiveOutput) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types.service_level_objective

    out["Slo"] = (
        aws_sdk_application_signals.types.service_level_objective.serialize_json(
            value["slo"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetServiceLevelObjectiveOutput:
    out: GetServiceLevelObjectiveOutput = {}  # type: ignore[typeddict-item]
    if "Slo" in data:
        import aws_sdk_application_signals.types.service_level_objective

        out["slo"] = (
            aws_sdk_application_signals.types.service_level_objective.deserialize_json(
                data["Slo"]
            )
        )
    else:
        raise DeserializationError("GetServiceLevelObjectiveOutput.slo required")
    return out
