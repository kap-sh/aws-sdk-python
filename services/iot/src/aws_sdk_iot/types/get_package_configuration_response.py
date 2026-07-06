"""Generated from Smithy shape ``com.amazonaws.iot#GetPackageConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.version_update_by_jobs_config


class GetPackageConfigurationResponse(TypedDict, closed=True):
    version_update_by_jobs_config: NotRequired[
        "aws_sdk_iot.types.version_update_by_jobs_config.VersionUpdateByJobsConfig"
    ]
    """<p>The version that is associated to a specific job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPackageConfigurationResponse) -> dict:
    out: dict = {}
    if "version_update_by_jobs_config" in value:
        import aws_sdk_iot.types.version_update_by_jobs_config

        out["versionUpdateByJobsConfig"] = (
            aws_sdk_iot.types.version_update_by_jobs_config.serialize_json(
                value["version_update_by_jobs_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPackageConfigurationResponse:
    out: GetPackageConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "versionUpdateByJobsConfig" in data:
        import aws_sdk_iot.types.version_update_by_jobs_config

        out["version_update_by_jobs_config"] = (
            aws_sdk_iot.types.version_update_by_jobs_config.deserialize_json(
                data["versionUpdateByJobsConfig"]
            )
        )
    return out
