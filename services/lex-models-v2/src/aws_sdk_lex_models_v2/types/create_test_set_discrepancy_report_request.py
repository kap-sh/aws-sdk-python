"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateTestSetDiscrepancyReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target


class CreateTestSetDiscrepancyReportRequest(TypedDict, closed=True):
    test_set_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The test set Id for the test set discrepancy report.</p>"""
    target: "aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target.TestSetDiscrepancyReportResourceTarget"
    """<p>The target bot for the test set discrepancy report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTestSetDiscrepancyReportRequest) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target

    out["target"] = (
        aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target.serialize_json(
            value["target"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateTestSetDiscrepancyReportRequest:
    out: CreateTestSetDiscrepancyReportRequest = {}  # type: ignore[typeddict-item]
    if "target" in data:
        import aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target

        out["target"] = (
            aws_sdk_lex_models_v2.types.test_set_discrepancy_report_resource_target.deserialize_json(
                data["target"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTestSetDiscrepancyReportRequest.target required"
        )
    return out
