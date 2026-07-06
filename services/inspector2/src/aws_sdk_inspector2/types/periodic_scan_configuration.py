"""Generated from Smithy shape ``com.amazonaws.inspector2#PeriodicScanConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.frequency_expression
    import aws_sdk_inspector2.types.periodic_scan_frequency


class PeriodicScanConfiguration(TypedDict, closed=True):
    frequency: NotRequired[
        "aws_sdk_inspector2.types.periodic_scan_frequency.PeriodicScanFrequency"
    ]
    """<p>The frequency at which periodic scans are performed (such as weekly or monthly).</p> <p>If you don't provide the <code>frequencyExpression</code> Amazon Inspector chooses day for the scan to run. If you provide the <code>frequencyExpression</code>, the schedule must match the specified <code>frequency</code>.</p>"""
    frequency_expression: NotRequired[
        "aws_sdk_inspector2.types.frequency_expression.FrequencyExpression"
    ]
    """<p>The schedule expression for periodic scans, in cron format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PeriodicScanConfiguration) -> dict:
    out: dict = {}
    if "frequency" in value:
        import aws_sdk_inspector2.types.periodic_scan_frequency

        out["frequency"] = (
            aws_sdk_inspector2.types.periodic_scan_frequency.serialize_json(
                value["frequency"]
            )
        )
    if "frequency_expression" in value:
        out["frequencyExpression"] = value["frequency_expression"]
    return out


def deserialize_json(data: dict) -> PeriodicScanConfiguration:
    out: PeriodicScanConfiguration = {}  # type: ignore[typeddict-item]
    if "frequency" in data:
        import aws_sdk_inspector2.types.periodic_scan_frequency

        out["frequency"] = (
            aws_sdk_inspector2.types.periodic_scan_frequency.deserialize_json(
                data["frequency"]
            )
        )
    if "frequencyExpression" in data:
        out["frequency_expression"] = data["frequencyExpression"]
    return out
