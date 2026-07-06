"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServiceLevelObjectivesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.next_token
    import aws_sdk_application_signals.types.service_level_objective_summaries


class ListServiceLevelObjectivesOutput(TypedDict, closed=True):
    slo_summaries: NotRequired[
        "aws_sdk_application_signals.types.service_level_objective_summaries.ServiceLevelObjectiveSummaries"
    ]
    """<p>An array of structures, where each structure contains information about one SLO.</p>"""
    next_token: NotRequired["aws_sdk_application_signals.types.next_token.NextToken"]
    """<p>Include this value in your next use of this API to get next set of service level objectives.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceLevelObjectivesOutput) -> dict:
    out: dict = {}
    if "slo_summaries" in value:
        import aws_sdk_application_signals.types.service_level_objective_summaries

        out["SloSummaries"] = (
            aws_sdk_application_signals.types.service_level_objective_summaries.serialize_json(
                value["slo_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceLevelObjectivesOutput:
    out: ListServiceLevelObjectivesOutput = {}  # type: ignore[typeddict-item]
    if "SloSummaries" in data:
        import aws_sdk_application_signals.types.service_level_objective_summaries

        out["slo_summaries"] = (
            aws_sdk_application_signals.types.service_level_objective_summaries.deserialize_json(
                data["SloSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
