"""Generated from Smithy shape ``com.amazonaws.sagemaker#SpaceIdleSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.idle_timeout_in_minutes


class SpaceIdleSettings(TypedDict):
    idle_timeout_in_minutes: NotRequired[
        "aws_sdk_sagemaker.types.idle_timeout_in_minutes.IdleTimeoutInMinutes"
    ]
    """<p>The time that SageMaker waits after the application becomes idle before shutting it down.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpaceIdleSettings) -> dict:
    out: dict = {}
    if "idle_timeout_in_minutes" in value:
        out["IdleTimeoutInMinutes"] = value["idle_timeout_in_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SpaceIdleSettings:
    out: SpaceIdleSettings = {}  # type: ignore[typeddict-item]
    if "IdleTimeoutInMinutes" in data:
        out["idle_timeout_in_minutes"] = data["IdleTimeoutInMinutes"]
    return out
