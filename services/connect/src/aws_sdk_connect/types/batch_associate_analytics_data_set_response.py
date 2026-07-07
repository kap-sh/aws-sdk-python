"""Generated from Smithy shape ``com.amazonaws.connect#BatchAssociateAnalyticsDataSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.analytics_data_association_results
    import aws_sdk_connect.types.error_results


class BatchAssociateAnalyticsDataSetResponse(TypedDict, closed=True):
    created: NotRequired[
        "aws_sdk_connect.types.analytics_data_association_results.AnalyticsDataAssociationResults"
    ]
    """<p>Information about associations that are successfully created: <code>DataSetId</code>, <code>TargetAccountId</code>, <code>ResourceShareId</code>, <code>ResourceShareArn</code>. </p>"""
    errors: NotRequired["aws_sdk_connect.types.error_results.ErrorResults"]
    """<p>A list of errors for datasets that aren't successfully associated with the target account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateAnalyticsDataSetResponse) -> dict:
    out: dict = {}
    if "created" in value:
        import aws_sdk_connect.types.analytics_data_association_results

        out["Created"] = (
            aws_sdk_connect.types.analytics_data_association_results.serialize_json(
                value["created"]
            )
        )
    if "errors" in value:
        import aws_sdk_connect.types.error_results

        out["Errors"] = aws_sdk_connect.types.error_results.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> BatchAssociateAnalyticsDataSetResponse:
    out: BatchAssociateAnalyticsDataSetResponse = {}  # type: ignore[typeddict-item]
    if "Created" in data:
        import aws_sdk_connect.types.analytics_data_association_results

        out["created"] = (
            aws_sdk_connect.types.analytics_data_association_results.deserialize_json(
                data["Created"]
            )
        )
    if "Errors" in data:
        import aws_sdk_connect.types.error_results

        out["errors"] = aws_sdk_connect.types.error_results.deserialize_json(
            data["Errors"]
        )
    return out
