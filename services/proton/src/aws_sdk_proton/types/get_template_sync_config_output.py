"""Generated from Smithy shape ``com.amazonaws.proton#GetTemplateSyncConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_proton.types.template_sync_config


class GetTemplateSyncConfigOutput(TypedDict, closed=True):
    template_sync_config: NotRequired[
        "aws_sdk_proton.types.template_sync_config.TemplateSyncConfig"
    ]
    """<p>The template sync configuration detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTemplateSyncConfigOutput) -> dict:
    out: dict = {}
    if "template_sync_config" in value:
        import aws_sdk_proton.types.template_sync_config

        out["templateSyncConfig"] = (
            aws_sdk_proton.types.template_sync_config.serialize_aws_json_1_0(
                value["template_sync_config"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTemplateSyncConfigOutput:
    out: GetTemplateSyncConfigOutput = {}  # type: ignore[typeddict-item]
    if "templateSyncConfig" in data:
        import aws_sdk_proton.types.template_sync_config

        out["template_sync_config"] = (
            aws_sdk_proton.types.template_sync_config.deserialize_aws_json_1_0(
                data["templateSyncConfig"]
            )
        )
    return out
