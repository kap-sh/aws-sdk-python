"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateTestSetDiscrepancyReportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target
    import aws_sdk_lex_models_v2.types.timestamp


class CreateTestSetDiscrepancyReportResponse(TypedDict):
    test_set_discrepancy_report_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the test set discrepancy report to describe.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The creation date and time for the test set discrepancy report.</p>"""
    test_set_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The test set Id for the test set discrepancy report.</p>"""
    target: NotRequired[
        "aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target.TestSetDiscrepancyReportResourceTarget"
    ]
    """<p>The target bot for the test set discrepancy report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTestSetDiscrepancyReportResponse) -> dict:
    out: dict = {}
    if "test_set_discrepancy_report_id" in value:
        out["testSetDiscrepancyReportId"] = value["test_set_discrepancy_report_id"]
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "test_set_id" in value:
        out["testSetId"] = value["test_set_id"]
    if "target" in value:
        import aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target

        out["target"] = (
            aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target.serialize_json(
                value["target"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateTestSetDiscrepancyReportResponse:
    out: CreateTestSetDiscrepancyReportResponse = {}  # type: ignore[typeddict-item]
    if "testSetDiscrepancyReportId" in data:
        out["test_set_discrepancy_report_id"] = data["testSetDiscrepancyReportId"]
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "testSetId" in data:
        out["test_set_id"] = data["testSetId"]
    if "target" in data:
        import aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target

        out["target"] = (
            aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target.deserialize_json(
                data["target"]
            )
        )
    return out
