"""Generated from Smithy shape ``com.amazonaws.sagemaker#SpaceAppLifecycleManagement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.space_idle_settings


class SpaceAppLifecycleManagement(TypedDict, closed=True):
    idle_settings: NotRequired[
        "capo_sagemaker.types.space_idle_settings.SpaceIdleSettings"
    ]
    """<p>Settings related to idle shutdown of Studio applications.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpaceAppLifecycleManagement) -> dict:
    out: dict = {}
    if "idle_settings" in value:
        import capo_sagemaker.types.space_idle_settings

        out["IdleSettings"] = (
            capo_sagemaker.types.space_idle_settings.serialize_aws_json_1_1(
                value["idle_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SpaceAppLifecycleManagement:
    out: SpaceAppLifecycleManagement = {}  # type: ignore[typeddict-item]
    if "IdleSettings" in data:
        import capo_sagemaker.types.space_idle_settings

        out["idle_settings"] = (
            capo_sagemaker.types.space_idle_settings.deserialize_aws_json_1_1(
                data["IdleSettings"]
            )
        )
    return out
