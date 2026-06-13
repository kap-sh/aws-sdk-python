"""Generated from Smithy shape ``com.amazonaws.applicationsignals#UpdateServiceLevelObjectiveOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.service_level_objective


class UpdateServiceLevelObjectiveOutput(TypedDict):
    slo: "aws_sdk_application_signals.types.service_level_objective.ServiceLevelObjective"
    """<p>A structure that contains information about the SLO that you just updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceLevelObjectiveOutput) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types.service_level_objective

    out["Slo"] = (
        aws_sdk_application_signals.types.service_level_objective.serialize_json(
            value["slo"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateServiceLevelObjectiveOutput:
    out: UpdateServiceLevelObjectiveOutput = {}  # type: ignore[typeddict-item]
    if "Slo" in data:
        import aws_sdk_application_signals.types.service_level_objective

        out["slo"] = (
            aws_sdk_application_signals.types.service_level_objective.deserialize_json(
                data["Slo"]
            )
        )
    else:
        raise DeserializationError("UpdateServiceLevelObjectiveOutput.slo required")
    return out
