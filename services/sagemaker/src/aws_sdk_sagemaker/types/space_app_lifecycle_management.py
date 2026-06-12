"""Generated from Smithy shape ``com.amazonaws.sagemaker#SpaceAppLifecycleManagement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.space_idle_settings


class SpaceAppLifecycleManagement(TypedDict):
    idle_settings: NotRequired[
        "aws_sdk_sagemaker.types.space_idle_settings.SpaceIdleSettings"
    ]
    """<p>Settings related to idle shutdown of Studio applications.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpaceAppLifecycleManagement) -> dict:
    out: dict = {}
    if "idle_settings" in value:
        import aws_sdk_sagemaker.types.space_idle_settings

        out["IdleSettings"] = (
            aws_sdk_sagemaker.types.space_idle_settings.serialize_aws_json_1_1(
                value["idle_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SpaceAppLifecycleManagement:
    out: SpaceAppLifecycleManagement = {}  # type: ignore[typeddict-item]
    if "IdleSettings" in data:
        import aws_sdk_sagemaker.types.space_idle_settings

        out["idle_settings"] = (
            aws_sdk_sagemaker.types.space_idle_settings.deserialize_aws_json_1_1(
                data["IdleSettings"]
            )
        )
    return out
