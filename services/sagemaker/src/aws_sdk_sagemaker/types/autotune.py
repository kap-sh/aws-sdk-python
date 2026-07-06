"""Generated from Smithy shape ``com.amazonaws.sagemaker#Autotune``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.autotune_mode


class Autotune(TypedDict, closed=True):
    mode: NotRequired["aws_sdk_sagemaker.types.autotune_mode.AutotuneMode"]
    """<p>Set <code>Mode</code> to <code>Enabled</code> if you want to use Autotune.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Autotune) -> dict:
    out: dict = {}
    if "mode" in value:
        import aws_sdk_sagemaker.types.autotune_mode

        out["Mode"] = aws_sdk_sagemaker.types.autotune_mode.serialize_aws_json_1_1(
            value["mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Autotune:
    out: Autotune = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        import aws_sdk_sagemaker.types.autotune_mode

        out["mode"] = aws_sdk_sagemaker.types.autotune_mode.deserialize_aws_json_1_1(
            data["Mode"]
        )
    return out
