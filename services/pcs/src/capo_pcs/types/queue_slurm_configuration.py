"""Generated from Smithy shape ``com.amazonaws.pcs#QueueSlurmConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.slurm_custom_settings


class QueueSlurmConfiguration(TypedDict, closed=True):
    slurm_custom_settings: NotRequired[
        "capo_pcs.types.slurm_custom_settings.SlurmCustomSettings"
    ]
    """<p>Additional Slurm-specific configuration that directly maps to Slurm settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueueSlurmConfiguration) -> dict:
    out: dict = {}
    if "slurm_custom_settings" in value:
        import capo_pcs.types.slurm_custom_settings

        out["slurmCustomSettings"] = (
            capo_pcs.types.slurm_custom_settings.serialize_aws_json_1_0(
                value["slurm_custom_settings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> QueueSlurmConfiguration:
    out: QueueSlurmConfiguration = {}  # type: ignore[typeddict-item]
    if "slurmCustomSettings" in data:
        import capo_pcs.types.slurm_custom_settings

        out["slurm_custom_settings"] = (
            capo_pcs.types.slurm_custom_settings.deserialize_aws_json_1_0(
                data["slurmCustomSettings"]
            )
        )
    return out
