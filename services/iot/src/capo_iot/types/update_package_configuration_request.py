"""Generated from Smithy shape ``com.amazonaws.iot#UpdatePackageConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.client_token
    import capo_iot.types.version_update_by_jobs_config


class UpdatePackageConfigurationRequest(TypedDict, closed=True):
    version_update_by_jobs_config: NotRequired[
        "capo_iot.types.version_update_by_jobs_config.VersionUpdateByJobsConfig"
    ]
    """<p>Configuration to manage job's package version reporting. This updates the thing's reserved named shadow that the job targets.</p>"""
    client_token: NotRequired["capo_iot.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageConfigurationRequest) -> dict:
    out: dict = {}
    if "version_update_by_jobs_config" in value:
        import capo_iot.types.version_update_by_jobs_config

        out["versionUpdateByJobsConfig"] = (
            capo_iot.types.version_update_by_jobs_config.serialize_json(
                value["version_update_by_jobs_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePackageConfigurationRequest:
    out: UpdatePackageConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "versionUpdateByJobsConfig" in data:
        import capo_iot.types.version_update_by_jobs_config

        out["version_update_by_jobs_config"] = (
            capo_iot.types.version_update_by_jobs_config.deserialize_json(
                data["versionUpdateByJobsConfig"]
            )
        )
    return out
