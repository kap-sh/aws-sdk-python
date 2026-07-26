"""Generated from Smithy shape ``com.amazonaws.sagemaker#SessionChainingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.enable_session_tag_chaining


class SessionChainingConfig(TypedDict, closed=True):
    enable_session_tag_chaining: NotRequired[
        "capo_sagemaker.types.enable_session_tag_chaining.EnableSessionTagChaining"
    ]
    """<p>Set to <code>True</code> to allow SageMaker to extract session tags from a training job creation role and reuse these tags when assuming the training job execution role.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionChainingConfig) -> dict:
    out: dict = {}
    if "enable_session_tag_chaining" in value:
        out["EnableSessionTagChaining"] = value["enable_session_tag_chaining"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionChainingConfig:
    out: SessionChainingConfig = {}  # type: ignore[typeddict-item]
    if "EnableSessionTagChaining" in data:
        out["enable_session_tag_chaining"] = data["EnableSessionTagChaining"]
    return out
