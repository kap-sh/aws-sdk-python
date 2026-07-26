"""Generated from Smithy shape ``com.amazonaws.sagemaker#CaptureOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.capture_mode


class CaptureOption(TypedDict, closed=True):
    capture_mode: NotRequired["capo_sagemaker.types.capture_mode.CaptureMode"]
    """<p>Specify the boundary of data to capture.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaptureOption) -> dict:
    out: dict = {}
    if "capture_mode" in value:
        import capo_sagemaker.types.capture_mode

        out["CaptureMode"] = capo_sagemaker.types.capture_mode.serialize_aws_json_1_1(
            value["capture_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CaptureOption:
    out: CaptureOption = {}  # type: ignore[typeddict-item]
    if "CaptureMode" in data:
        import capo_sagemaker.types.capture_mode

        out["capture_mode"] = (
            capo_sagemaker.types.capture_mode.deserialize_aws_json_1_1(
                data["CaptureMode"]
            )
        )
    return out
