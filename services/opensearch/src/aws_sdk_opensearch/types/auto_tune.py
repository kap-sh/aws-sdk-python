"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTune``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.auto_tune_details
    import aws_sdk_opensearch.types.auto_tune_type


class AutoTune(TypedDict, closed=True):
    auto_tune_type: NotRequired["aws_sdk_opensearch.types.auto_tune_type.AutoTuneType"]
    """<p>The type of Auto-Tune action.</p>"""
    auto_tune_details: NotRequired[
        "aws_sdk_opensearch.types.auto_tune_details.AutoTuneDetails"
    ]
    """<p>Details about an Auto-Tune action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTune) -> dict:
    out: dict = {}
    if "auto_tune_type" in value:
        import aws_sdk_opensearch.types.auto_tune_type

        out["AutoTuneType"] = aws_sdk_opensearch.types.auto_tune_type.serialize_json(
            value["auto_tune_type"]
        )
    if "auto_tune_details" in value:
        import aws_sdk_opensearch.types.auto_tune_details

        out["AutoTuneDetails"] = (
            aws_sdk_opensearch.types.auto_tune_details.serialize_json(
                value["auto_tune_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutoTune:
    out: AutoTune = {}  # type: ignore[typeddict-item]
    if "AutoTuneType" in data:
        import aws_sdk_opensearch.types.auto_tune_type

        out["auto_tune_type"] = (
            aws_sdk_opensearch.types.auto_tune_type.deserialize_json(
                data["AutoTuneType"]
            )
        )
    if "AutoTuneDetails" in data:
        import aws_sdk_opensearch.types.auto_tune_details

        out["auto_tune_details"] = (
            aws_sdk_opensearch.types.auto_tune_details.deserialize_json(
                data["AutoTuneDetails"]
            )
        )
    return out
