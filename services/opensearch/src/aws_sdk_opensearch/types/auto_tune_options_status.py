"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneOptionsStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.auto_tune_options
    import aws_sdk_opensearch.types.auto_tune_status


class AutoTuneOptionsStatus(TypedDict):
    options: NotRequired["aws_sdk_opensearch.types.auto_tune_options.AutoTuneOptions"]
    """<p>Auto-Tune settings for updating a domain.</p>"""
    status: NotRequired["aws_sdk_opensearch.types.auto_tune_status.AutoTuneStatus"]
    """<p>The current status of Auto-Tune for a domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneOptionsStatus) -> dict:
    out: dict = {}
    if "options" in value:
        import aws_sdk_opensearch.types.auto_tune_options

        out["Options"] = aws_sdk_opensearch.types.auto_tune_options.serialize_json(
            value["options"]
        )
    if "status" in value:
        import aws_sdk_opensearch.types.auto_tune_status

        out["Status"] = aws_sdk_opensearch.types.auto_tune_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> AutoTuneOptionsStatus:
    out: AutoTuneOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_opensearch.types.auto_tune_options

        out["options"] = aws_sdk_opensearch.types.auto_tune_options.deserialize_json(
            data["Options"]
        )
    if "Status" in data:
        import aws_sdk_opensearch.types.auto_tune_status

        out["status"] = aws_sdk_opensearch.types.auto_tune_status.deserialize_json(
            data["Status"]
        )
    return out
