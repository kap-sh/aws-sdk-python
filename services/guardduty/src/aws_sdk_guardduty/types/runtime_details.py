"""Generated from Smithy shape ``com.amazonaws.guardduty#RuntimeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.process_details
    import aws_sdk_guardduty.types.runtime_context


class RuntimeDetails(TypedDict, closed=True):
    process: NotRequired["aws_sdk_guardduty.types.process_details.ProcessDetails"]
    """<p>Information about the observed process.</p>"""
    context: NotRequired["aws_sdk_guardduty.types.runtime_context.RuntimeContext"]
    """<p>Additional information about the suspicious activity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeDetails) -> dict:
    out: dict = {}
    if "process" in value:
        import aws_sdk_guardduty.types.process_details

        out["process"] = aws_sdk_guardduty.types.process_details.serialize_json(
            value["process"]
        )
    if "context" in value:
        import aws_sdk_guardduty.types.runtime_context

        out["context"] = aws_sdk_guardduty.types.runtime_context.serialize_json(
            value["context"]
        )
    return out


def deserialize_json(data: dict) -> RuntimeDetails:
    out: RuntimeDetails = {}  # type: ignore[typeddict-item]
    if "process" in data:
        import aws_sdk_guardduty.types.process_details

        out["process"] = aws_sdk_guardduty.types.process_details.deserialize_json(
            data["process"]
        )
    if "context" in data:
        import aws_sdk_guardduty.types.runtime_context

        out["context"] = aws_sdk_guardduty.types.runtime_context.deserialize_json(
            data["context"]
        )
    return out
