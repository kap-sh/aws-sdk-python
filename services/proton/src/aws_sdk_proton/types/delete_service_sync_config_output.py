"""Generated from Smithy shape ``com.amazonaws.proton#DeleteServiceSyncConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_proton.types.service_sync_config


class DeleteServiceSyncConfigOutput(TypedDict, closed=True):
    service_sync_config: NotRequired[
        "aws_sdk_proton.types.service_sync_config.ServiceSyncConfig"
    ]
    """<p>The detailed data for the service sync config.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteServiceSyncConfigOutput) -> dict:
    out: dict = {}
    if "service_sync_config" in value:
        import aws_sdk_proton.types.service_sync_config

        out["serviceSyncConfig"] = (
            aws_sdk_proton.types.service_sync_config.serialize_aws_json_1_0(
                value["service_sync_config"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteServiceSyncConfigOutput:
    out: DeleteServiceSyncConfigOutput = {}  # type: ignore[typeddict-item]
    if "serviceSyncConfig" in data:
        import aws_sdk_proton.types.service_sync_config

        out["service_sync_config"] = (
            aws_sdk_proton.types.service_sync_config.deserialize_aws_json_1_0(
                data["serviceSyncConfig"]
            )
        )
    return out
