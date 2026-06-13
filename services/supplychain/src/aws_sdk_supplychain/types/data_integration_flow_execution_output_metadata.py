"""Generated from Smithy shape ``com.amazonaws.supplychain#DataIntegrationFlowExecutionOutputMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow_execution_diagnostic_reports_root_s3_uri


class DataIntegrationFlowExecutionOutputMetadata(TypedDict):
    diagnostic_reports_root_s3_uri: NotRequired[
        "aws_sdk_supplychain.types.data_integration_flow_execution_diagnostic_reports_root_s3_uri.DataIntegrationFlowExecutionDiagnosticReportsRootS3URI"
    ]
    """<p>The S3 URI under which all diagnostic files (such as deduped records if any) are stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataIntegrationFlowExecutionOutputMetadata) -> dict:
    out: dict = {}
    if "diagnostic_reports_root_s3_uri" in value:
        out["diagnosticReportsRootS3URI"] = value["diagnostic_reports_root_s3_uri"]
    return out


def deserialize_json(data: dict) -> DataIntegrationFlowExecutionOutputMetadata:
    out: DataIntegrationFlowExecutionOutputMetadata = {}  # type: ignore[typeddict-item]
    if "diagnosticReportsRootS3URI" in data:
        out["diagnostic_reports_root_s3_uri"] = data["diagnosticReportsRootS3URI"]
    return out
