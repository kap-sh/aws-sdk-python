"""Generated from Smithy shape ``com.amazonaws.lakeformation#BatchPermissionsFailureEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.batch_permissions_request_entry
    import capo_lakeformation.types.error_detail


class BatchPermissionsFailureEntry(TypedDict, closed=True):
    request_entry: NotRequired[
        "capo_lakeformation.types.batch_permissions_request_entry.BatchPermissionsRequestEntry"
    ]
    """<p>An identifier for an entry of the batch request.</p>"""
    error: NotRequired["capo_lakeformation.types.error_detail.ErrorDetail"]
    """<p>An error message that applies to the failure of the entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPermissionsFailureEntry) -> dict:
    out: dict = {}
    if "request_entry" in value:
        import capo_lakeformation.types.batch_permissions_request_entry

        out["RequestEntry"] = (
            capo_lakeformation.types.batch_permissions_request_entry.serialize_json(
                value["request_entry"]
            )
        )
    if "error" in value:
        import capo_lakeformation.types.error_detail

        out["Error"] = capo_lakeformation.types.error_detail.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> BatchPermissionsFailureEntry:
    out: BatchPermissionsFailureEntry = {}  # type: ignore[typeddict-item]
    if "RequestEntry" in data:
        import capo_lakeformation.types.batch_permissions_request_entry

        out["request_entry"] = (
            capo_lakeformation.types.batch_permissions_request_entry.deserialize_json(
                data["RequestEntry"]
            )
        )
    if "Error" in data:
        import capo_lakeformation.types.error_detail

        out["error"] = capo_lakeformation.types.error_detail.deserialize_json(
            data["Error"]
        )
    return out
