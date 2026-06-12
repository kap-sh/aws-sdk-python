"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceSeverityBreakdown``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer


class ResourceSeverityBreakdown(TypedDict):
    other: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of findings not in any of the severity categories.</p>"""
    fatal: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of findings with a severity level of fatal.</p>"""
    critical: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of findings with a severity level of critical.</p>"""
    high: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of findings with a severity level of high.</p>"""
    medium: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of findings with a severity level of medium.</p>"""
    low: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of findings with a severity level of low.</p>"""
    informational: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of findings that provide security-related information.</p>"""
    unknown: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of findings with a severity level cannot be determined.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSeverityBreakdown) -> dict:
    out: dict = {}
    if "other" in value:
        out["Other"] = value["other"]
    if "fatal" in value:
        out["Fatal"] = value["fatal"]
    if "critical" in value:
        out["Critical"] = value["critical"]
    if "high" in value:
        out["High"] = value["high"]
    if "medium" in value:
        out["Medium"] = value["medium"]
    if "low" in value:
        out["Low"] = value["low"]
    if "informational" in value:
        out["Informational"] = value["informational"]
    if "unknown" in value:
        out["Unknown"] = value["unknown"]
    return out


def deserialize_json(data: dict) -> ResourceSeverityBreakdown:
    out: ResourceSeverityBreakdown = {}  # type: ignore[typeddict-item]
    if "Other" in data:
        out["other"] = data["Other"]
    if "Fatal" in data:
        out["fatal"] = data["Fatal"]
    if "Critical" in data:
        out["critical"] = data["Critical"]
    if "High" in data:
        out["high"] = data["High"]
    if "Medium" in data:
        out["medium"] = data["Medium"]
    if "Low" in data:
        out["low"] = data["Low"]
    if "Informational" in data:
        out["informational"] = data["Informational"]
    if "Unknown" in data:
        out["unknown"] = data["Unknown"]
    return out
