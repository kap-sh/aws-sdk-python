"""Generated from Smithy shape ``com.amazonaws.medialive#OutputLockingSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.disabled_locking_settings
    import capo_medialive.types.epoch_locking_settings
    import capo_medialive.types.pipeline_locking_settings


class OutputLockingSettings(TypedDict, closed=True):
    epoch_locking_settings: NotRequired[
        "capo_medialive.types.epoch_locking_settings.EpochLockingSettings"
    ]
    pipeline_locking_settings: NotRequired[
        "capo_medialive.types.pipeline_locking_settings.PipelineLockingSettings"
    ]
    disabled_locking_settings: NotRequired[
        "capo_medialive.types.disabled_locking_settings.DisabledLockingSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: OutputLockingSettings) -> dict:
    out: dict = {}
    if "epoch_locking_settings" in value:
        import capo_medialive.types.epoch_locking_settings

        out["epochLockingSettings"] = (
            capo_medialive.types.epoch_locking_settings.serialize_json(
                value["epoch_locking_settings"]
            )
        )
    if "pipeline_locking_settings" in value:
        import capo_medialive.types.pipeline_locking_settings

        out["pipelineLockingSettings"] = (
            capo_medialive.types.pipeline_locking_settings.serialize_json(
                value["pipeline_locking_settings"]
            )
        )
    if "disabled_locking_settings" in value:
        import capo_medialive.types.disabled_locking_settings

        out["disabledLockingSettings"] = (
            capo_medialive.types.disabled_locking_settings.serialize_json(
                value["disabled_locking_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutputLockingSettings:
    out: OutputLockingSettings = {}  # type: ignore[typeddict-item]
    if "epochLockingSettings" in data:
        import capo_medialive.types.epoch_locking_settings

        out["epoch_locking_settings"] = (
            capo_medialive.types.epoch_locking_settings.deserialize_json(
                data["epochLockingSettings"]
            )
        )
    if "pipelineLockingSettings" in data:
        import capo_medialive.types.pipeline_locking_settings

        out["pipeline_locking_settings"] = (
            capo_medialive.types.pipeline_locking_settings.deserialize_json(
                data["pipelineLockingSettings"]
            )
        )
    if "disabledLockingSettings" in data:
        import capo_medialive.types.disabled_locking_settings

        out["disabled_locking_settings"] = (
            capo_medialive.types.disabled_locking_settings.deserialize_json(
                data["disabledLockingSettings"]
            )
        )
    return out
