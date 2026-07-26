"""Generated from Smithy shape ``com.amazonaws.lakeformation#UpdateTableStorageOptimizerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.result


class UpdateTableStorageOptimizerResponse(TypedDict, closed=True):
    result: NotRequired["capo_lakeformation.types.result.Result"]
    """<p>A response indicating the success of failure of the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTableStorageOptimizerResponse) -> dict:
    out: dict = {}
    if "result" in value:
        out["Result"] = value["result"]
    return out


def deserialize_json(data: dict) -> UpdateTableStorageOptimizerResponse:
    out: UpdateTableStorageOptimizerResponse = {}  # type: ignore[typeddict-item]
    if "Result" in data:
        out["result"] = data["Result"]
    return out
