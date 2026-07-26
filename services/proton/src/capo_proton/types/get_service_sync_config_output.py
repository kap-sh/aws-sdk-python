"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceSyncConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.service_sync_config


class GetServiceSyncConfigOutput(TypedDict, closed=True):
    service_sync_config: NotRequired[
        "capo_proton.types.service_sync_config.ServiceSyncConfig"
    ]
    """<p>The detailed data of the requested service sync configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceSyncConfigOutput) -> dict:
    out: dict = {}
    if "service_sync_config" in value:
        import capo_proton.types.service_sync_config

        out["serviceSyncConfig"] = (
            capo_proton.types.service_sync_config.serialize_aws_json_1_0(
                value["service_sync_config"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceSyncConfigOutput:
    out: GetServiceSyncConfigOutput = {}  # type: ignore[typeddict-item]
    if "serviceSyncConfig" in data:
        import capo_proton.types.service_sync_config

        out["service_sync_config"] = (
            capo_proton.types.service_sync_config.deserialize_aws_json_1_0(
                data["serviceSyncConfig"]
            )
        )
    return out
