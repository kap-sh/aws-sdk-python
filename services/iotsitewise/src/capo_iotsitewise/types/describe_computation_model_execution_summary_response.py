"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeComputationModelExecutionSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.computation_model_execution_summary
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.resolve_to


class DescribeComputationModelExecutionSummaryResponse(TypedDict, closed=True):
    computation_model_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the computation model.</p>"""
    resolve_to: NotRequired["capo_iotsitewise.types.resolve_to.ResolveTo"]
    """<p>The detailed resource this execution summary resolves to.</p>"""
    computation_model_execution_summary: "capo_iotsitewise.types.computation_model_execution_summary.ComputationModelExecutionSummary"
    """<p>Contains the execution summary of the computation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeComputationModelExecutionSummaryResponse) -> dict:
    out: dict = {}
    out["computationModelId"] = value["computation_model_id"]
    if "resolve_to" in value:
        import capo_iotsitewise.types.resolve_to

        out["resolveTo"] = capo_iotsitewise.types.resolve_to.serialize_json(
            value["resolve_to"]
        )
    import capo_iotsitewise.types.computation_model_execution_summary

    out["computationModelExecutionSummary"] = (
        capo_iotsitewise.types.computation_model_execution_summary.serialize_json(
            value["computation_model_execution_summary"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeComputationModelExecutionSummaryResponse:
    out: DescribeComputationModelExecutionSummaryResponse = {}  # type: ignore[typeddict-item]
    if "computationModelId" in data:
        out["computation_model_id"] = data["computationModelId"]
    else:
        raise DeserializationError(
            "DescribeComputationModelExecutionSummaryResponse.computation_model_id required"
        )
    if "resolveTo" in data:
        import capo_iotsitewise.types.resolve_to

        out["resolve_to"] = capo_iotsitewise.types.resolve_to.deserialize_json(
            data["resolveTo"]
        )
    if "computationModelExecutionSummary" in data:
        import capo_iotsitewise.types.computation_model_execution_summary

        out["computation_model_execution_summary"] = (
            capo_iotsitewise.types.computation_model_execution_summary.deserialize_json(
                data["computationModelExecutionSummary"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeComputationModelExecutionSummaryResponse.computation_model_execution_summary required"
        )
    return out
