"""Generated from Smithy shape ``com.amazonaws.proton#DeleteTemplateSyncConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_proton.types.template_sync_config


class DeleteTemplateSyncConfigOutput(TypedDict, closed=True):
    template_sync_config: NotRequired[
        "aws_sdk_proton.types.template_sync_config.TemplateSyncConfig"
    ]
    """<p>The template sync configuration detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteTemplateSyncConfigOutput) -> dict:
    out: dict = {}
    if "template_sync_config" in value:
        import aws_sdk_proton.types.template_sync_config

        out["templateSyncConfig"] = (
            aws_sdk_proton.types.template_sync_config.serialize_aws_json_1_0(
                value["template_sync_config"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteTemplateSyncConfigOutput:
    out: DeleteTemplateSyncConfigOutput = {}  # type: ignore[typeddict-item]
    if "templateSyncConfig" in data:
        import aws_sdk_proton.types.template_sync_config

        out["template_sync_config"] = (
            aws_sdk_proton.types.template_sync_config.deserialize_aws_json_1_0(
                data["templateSyncConfig"]
            )
        )
    return out
