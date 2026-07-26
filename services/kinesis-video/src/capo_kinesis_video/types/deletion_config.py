"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DeletionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.delete_after_upload
    import capo_kinesis_video.types.edge_retention_in_hours
    import capo_kinesis_video.types.local_size_config


class DeletionConfig(TypedDict, closed=True):
    edge_retention_in_hours: NotRequired[
        "capo_kinesis_video.types.edge_retention_in_hours.EdgeRetentionInHours"
    ]
    """<p>The number of hours that you want to retain the data in the stream on the Edge Agent. The default value of the retention time is 720 hours, which translates to 30 days.</p>"""
    local_size_config: NotRequired[
        "capo_kinesis_video.types.local_size_config.LocalSizeConfig"
    ]
    """<p>The value of the local size required in order to delete the edge configuration.</p>"""
    delete_after_upload: NotRequired[
        "capo_kinesis_video.types.delete_after_upload.DeleteAfterUpload"
    ]
    """<p>The <code>boolean</code> value used to indicate whether or not you want to mark the media for deletion, once it has been uploaded to the Kinesis Video Stream cloud. The media files can be deleted if any of the deletion configuration values are set to <code>true</code>, such as when the limit for the <code>EdgeRetentionInHours</code>, or the <code>MaxLocalMediaSizeInMB</code>, has been reached. </p> <p>Since the default value is set to <code>true</code>, configure the uploader schedule such that the media files are not being deleted before they are initially uploaded to the Amazon Web Services cloud.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletionConfig) -> dict:
    out: dict = {}
    if "edge_retention_in_hours" in value:
        out["EdgeRetentionInHours"] = value["edge_retention_in_hours"]
    if "local_size_config" in value:
        import capo_kinesis_video.types.local_size_config

        out["LocalSizeConfig"] = (
            capo_kinesis_video.types.local_size_config.serialize_json(
                value["local_size_config"]
            )
        )
    if "delete_after_upload" in value:
        out["DeleteAfterUpload"] = value["delete_after_upload"]
    return out


def deserialize_json(data: dict) -> DeletionConfig:
    out: DeletionConfig = {}  # type: ignore[typeddict-item]
    if "EdgeRetentionInHours" in data:
        out["edge_retention_in_hours"] = data["EdgeRetentionInHours"]
    if "LocalSizeConfig" in data:
        import capo_kinesis_video.types.local_size_config

        out["local_size_config"] = (
            capo_kinesis_video.types.local_size_config.deserialize_json(
                data["LocalSizeConfig"]
            )
        )
    if "DeleteAfterUpload" in data:
        out["delete_after_upload"] = data["DeleteAfterUpload"]
    return out
