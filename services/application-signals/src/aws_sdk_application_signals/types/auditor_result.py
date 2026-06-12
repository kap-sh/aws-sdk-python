"""Generated from Smithy shape ``com.amazonaws.applicationsignals#AuditorResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_application_signals.types.data_map
    import aws_sdk_application_signals.types.severity

class AuditorResult(TypedDict):
    auditor: NotRequired["str"]
    """<p>The name of the auditor algorithm that generated this result.</p>"""
    description: NotRequired["str"]
    """<p>A detailed description of the audit finding, explaining what was observed and potential implications.</p>"""
    data: NotRequired["aws_sdk_application_signals.types.data_map.DataMap"]
    """<p>This is a string-to-string map. It contains additional data about the result of an automated audit analysis.</p>"""
    severity: NotRequired["aws_sdk_application_signals.types.severity.Severity"]
    """<p>The severity level of this audit finding, indicating the importance and potential impact of the issue.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AuditorResult) -> dict:
    out: dict = {}
    if "auditor" in value:
        out["Auditor"] = value["auditor"]
    if "description" in value:
        out["Description"] = value["description"]
    if "data" in value:
        import aws_sdk_application_signals.types.data_map
        out["Data"] = aws_sdk_application_signals.types.data_map.serialize_json(value["data"])
    if "severity" in value:
        import aws_sdk_application_signals.types.severity
        out["Severity"] = aws_sdk_application_signals.types.severity.serialize_json(value["severity"])
    return out


def deserialize_json(data: dict) -> AuditorResult:
    out: AuditorResult = {}  # type: ignore[typeddict-item]
    if "Auditor" in data:
        out["auditor"] = data["Auditor"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Data" in data:
        import aws_sdk_application_signals.types.data_map
        out["data"] = aws_sdk_application_signals.types.data_map.deserialize_json(data["Data"])
    if "Severity" in data:
        import aws_sdk_application_signals.types.severity
        out["severity"] = aws_sdk_application_signals.types.severity.deserialize_json(data["Severity"])
    return out