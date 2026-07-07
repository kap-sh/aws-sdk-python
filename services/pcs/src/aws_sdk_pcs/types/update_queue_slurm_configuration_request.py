"""Generated from Smithy shape ``com.amazonaws.pcs#UpdateQueueSlurmConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pcs.types.slurm_custom_settings


class UpdateQueueSlurmConfigurationRequest(TypedDict, closed=True):
    slurm_custom_settings: NotRequired[
        "aws_sdk_pcs.types.slurm_custom_settings.SlurmCustomSettings"
    ]
    """<p>Additional Slurm-specific configuration that directly maps to Slurm settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateQueueSlurmConfigurationRequest) -> dict:
    out: dict = {}
    if "slurm_custom_settings" in value:
        import aws_sdk_pcs.types.slurm_custom_settings

        out["slurmCustomSettings"] = (
            aws_sdk_pcs.types.slurm_custom_settings.serialize_aws_json_1_0(
                value["slurm_custom_settings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateQueueSlurmConfigurationRequest:
    out: UpdateQueueSlurmConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "slurmCustomSettings" in data:
        import aws_sdk_pcs.types.slurm_custom_settings

        out["slurm_custom_settings"] = (
            aws_sdk_pcs.types.slurm_custom_settings.deserialize_aws_json_1_0(
                data["slurmCustomSettings"]
            )
        )
    return out
