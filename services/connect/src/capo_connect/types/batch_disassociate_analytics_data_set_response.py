"""Generated from Smithy shape ``com.amazonaws.connect#BatchDisassociateAnalyticsDataSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_set_ids
    import capo_connect.types.error_results


class BatchDisassociateAnalyticsDataSetResponse(TypedDict, closed=True):
    deleted: NotRequired["capo_connect.types.data_set_ids.DataSetIds"]
    """<p>An array of successfully disassociated dataset identifiers.</p>"""
    errors: NotRequired["capo_connect.types.error_results.ErrorResults"]
    """<p>A list of errors for any datasets not successfully removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateAnalyticsDataSetResponse) -> dict:
    out: dict = {}
    if "deleted" in value:
        import capo_connect.types.data_set_ids

        out["Deleted"] = capo_connect.types.data_set_ids.serialize_json(
            value["deleted"]
        )
    if "errors" in value:
        import capo_connect.types.error_results

        out["Errors"] = capo_connect.types.error_results.serialize_json(value["errors"])
    return out


def deserialize_json(data: dict) -> BatchDisassociateAnalyticsDataSetResponse:
    out: BatchDisassociateAnalyticsDataSetResponse = {}  # type: ignore[typeddict-item]
    if "Deleted" in data:
        import capo_connect.types.data_set_ids

        out["deleted"] = capo_connect.types.data_set_ids.deserialize_json(
            data["Deleted"]
        )
    if "Errors" in data:
        import capo_connect.types.error_results

        out["errors"] = capo_connect.types.error_results.deserialize_json(
            data["Errors"]
        )
    return out
