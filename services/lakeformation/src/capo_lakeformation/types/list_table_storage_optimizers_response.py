"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListTableStorageOptimizersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.storage_optimizer_list
    import capo_lakeformation.types.token


class ListTableStorageOptimizersResponse(TypedDict, closed=True):
    storage_optimizer_list: NotRequired[
        "capo_lakeformation.types.storage_optimizer_list.StorageOptimizerList"
    ]
    """<p>A list of the storage optimizers associated with a table.</p>"""
    next_token: NotRequired["capo_lakeformation.types.token.Token"]
    """<p>A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTableStorageOptimizersResponse) -> dict:
    out: dict = {}
    if "storage_optimizer_list" in value:
        import capo_lakeformation.types.storage_optimizer_list

        out["StorageOptimizerList"] = (
            capo_lakeformation.types.storage_optimizer_list.serialize_json(
                value["storage_optimizer_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTableStorageOptimizersResponse:
    out: ListTableStorageOptimizersResponse = {}  # type: ignore[typeddict-item]
    if "StorageOptimizerList" in data:
        import capo_lakeformation.types.storage_optimizer_list

        out["storage_optimizer_list"] = (
            capo_lakeformation.types.storage_optimizer_list.deserialize_json(
                data["StorageOptimizerList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
