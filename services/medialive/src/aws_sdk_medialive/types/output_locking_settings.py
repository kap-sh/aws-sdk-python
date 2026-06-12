"""Generated from Smithy shape ``com.amazonaws.medialive#OutputLockingSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.disabled_locking_settings
    import aws_sdk_medialive.types.epoch_locking_settings
    import aws_sdk_medialive.types.pipeline_locking_settings


class OutputLockingSettings(TypedDict):
    epoch_locking_settings: NotRequired[
        "aws_sdk_medialive.types.epoch_locking_settings.EpochLockingSettings"
    ]
    pipeline_locking_settings: NotRequired[
        "aws_sdk_medialive.types.pipeline_locking_settings.PipelineLockingSettings"
    ]
    disabled_locking_settings: NotRequired[
        "aws_sdk_medialive.types.disabled_locking_settings.DisabledLockingSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: OutputLockingSettings) -> dict:
    out: dict = {}
    if "epoch_locking_settings" in value:
        import aws_sdk_medialive.types.epoch_locking_settings

        out["epochLockingSettings"] = (
            aws_sdk_medialive.types.epoch_locking_settings.serialize_json(
                value["epoch_locking_settings"]
            )
        )
    if "pipeline_locking_settings" in value:
        import aws_sdk_medialive.types.pipeline_locking_settings

        out["pipelineLockingSettings"] = (
            aws_sdk_medialive.types.pipeline_locking_settings.serialize_json(
                value["pipeline_locking_settings"]
            )
        )
    if "disabled_locking_settings" in value:
        import aws_sdk_medialive.types.disabled_locking_settings

        out["disabledLockingSettings"] = (
            aws_sdk_medialive.types.disabled_locking_settings.serialize_json(
                value["disabled_locking_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutputLockingSettings:
    out: OutputLockingSettings = {}  # type: ignore[typeddict-item]
    if "epochLockingSettings" in data:
        import aws_sdk_medialive.types.epoch_locking_settings

        out["epoch_locking_settings"] = (
            aws_sdk_medialive.types.epoch_locking_settings.deserialize_json(
                data["epochLockingSettings"]
            )
        )
    if "pipelineLockingSettings" in data:
        import aws_sdk_medialive.types.pipeline_locking_settings

        out["pipeline_locking_settings"] = (
            aws_sdk_medialive.types.pipeline_locking_settings.deserialize_json(
                data["pipelineLockingSettings"]
            )
        )
    if "disabledLockingSettings" in data:
        import aws_sdk_medialive.types.disabled_locking_settings

        out["disabled_locking_settings"] = (
            aws_sdk_medialive.types.disabled_locking_settings.deserialize_json(
                data["disabledLockingSettings"]
            )
        )
    return out
