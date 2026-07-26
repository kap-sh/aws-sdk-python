"""Generated from Smithy shape ``com.amazonaws.rdsdata#BatchExecuteStatementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rds_data.types.update_results


class BatchExecuteStatementResponse(TypedDict, closed=True):
    update_results: NotRequired["capo_rds_data.types.update_results.UpdateResults"]
    """<p>The execution results of each batch entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchExecuteStatementResponse) -> dict:
    out: dict = {}
    if "update_results" in value:
        import capo_rds_data.types.update_results

        out["updateResults"] = capo_rds_data.types.update_results.serialize_json(
            value["update_results"]
        )
    return out


def deserialize_json(data: dict) -> BatchExecuteStatementResponse:
    out: BatchExecuteStatementResponse = {}  # type: ignore[typeddict-item]
    if "updateResults" in data:
        import capo_rds_data.types.update_results

        out["update_results"] = capo_rds_data.types.update_results.deserialize_json(
            data["updateResults"]
        )
    return out
