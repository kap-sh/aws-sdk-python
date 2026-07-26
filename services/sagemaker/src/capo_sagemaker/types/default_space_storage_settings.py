"""Generated from Smithy shape ``com.amazonaws.sagemaker#DefaultSpaceStorageSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.default_ebs_storage_settings


class DefaultSpaceStorageSettings(TypedDict, closed=True):
    default_ebs_storage_settings: NotRequired[
        "capo_sagemaker.types.default_ebs_storage_settings.DefaultEbsStorageSettings"
    ]
    """<p>The default EBS storage settings for a space.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultSpaceStorageSettings) -> dict:
    out: dict = {}
    if "default_ebs_storage_settings" in value:
        import capo_sagemaker.types.default_ebs_storage_settings

        out["DefaultEbsStorageSettings"] = (
            capo_sagemaker.types.default_ebs_storage_settings.serialize_aws_json_1_1(
                value["default_ebs_storage_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DefaultSpaceStorageSettings:
    out: DefaultSpaceStorageSettings = {}  # type: ignore[typeddict-item]
    if "DefaultEbsStorageSettings" in data:
        import capo_sagemaker.types.default_ebs_storage_settings

        out["default_ebs_storage_settings"] = (
            capo_sagemaker.types.default_ebs_storage_settings.deserialize_aws_json_1_1(
                data["DefaultEbsStorageSettings"]
            )
        )
    return out
