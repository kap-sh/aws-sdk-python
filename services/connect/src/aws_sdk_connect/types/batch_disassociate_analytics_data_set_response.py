"""Generated from Smithy shape ``com.amazonaws.connect#BatchDisassociateAnalyticsDataSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_set_ids
    import aws_sdk_connect.types.error_results


class BatchDisassociateAnalyticsDataSetResponse(TypedDict):
    deleted: NotRequired["aws_sdk_connect.types.data_set_ids.DataSetIds"]
    """<p>An array of successfully disassociated dataset identifiers.</p>"""
    errors: NotRequired["aws_sdk_connect.types.error_results.ErrorResults"]
    """<p>A list of errors for any datasets not successfully removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateAnalyticsDataSetResponse) -> dict:
    out: dict = {}
    if "deleted" in value:
        import aws_sdk_connect.types.data_set_ids

        out["Deleted"] = aws_sdk_connect.types.data_set_ids.serialize_json(
            value["deleted"]
        )
    if "errors" in value:
        import aws_sdk_connect.types.error_results

        out["Errors"] = aws_sdk_connect.types.error_results.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> BatchDisassociateAnalyticsDataSetResponse:
    out: BatchDisassociateAnalyticsDataSetResponse = {}  # type: ignore[typeddict-item]
    if "Deleted" in data:
        import aws_sdk_connect.types.data_set_ids

        out["deleted"] = aws_sdk_connect.types.data_set_ids.deserialize_json(
            data["Deleted"]
        )
    if "Errors" in data:
        import aws_sdk_connect.types.error_results

        out["errors"] = aws_sdk_connect.types.error_results.deserialize_json(
            data["Errors"]
        )
    return out
