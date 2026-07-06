"""Generated from Smithy shape ``com.amazonaws.omics#StartRunBatchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.batch_name
    import aws_sdk_omics.types.batch_request_id
    import aws_sdk_omics.types.batch_run_settings
    import aws_sdk_omics.types.default_run_setting
    import aws_sdk_omics.types.tag_map


class StartRunBatchRequest(TypedDict, closed=True):
    batch_name: NotRequired["aws_sdk_omics.types.batch_name.BatchName"]
    """<p>An optional user-friendly name for the run batch.</p>"""
    request_id: "aws_sdk_omics.types.batch_request_id.BatchRequestId"
    """<p>A client token used to deduplicate retry requests and prevent duplicate batches from being created.</p>"""
    tags: NotRequired["aws_sdk_omics.types.tag_map.TagMap"]
    """<p>AWS tags to associate with the batch resource. These tags are not inherited by individual runs. To tag individual runs, use <code>defaultRunSetting.runTags</code>.</p>"""
    default_run_setting: "aws_sdk_omics.types.default_run_setting.DefaultRunSetting"
    """<p>Shared configuration applied to all runs in the batch. See <code>DefaultRunSetting</code>.</p>"""
    batch_run_settings: "aws_sdk_omics.types.batch_run_settings.BatchRunSettings"
    """<p>The individual run configurations. Specify exactly one of <code>inlineSettings</code> or <code>s3UriSettings</code>. See <code>BatchRunSettings</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRunBatchRequest) -> dict:
    out: dict = {}
    if "batch_name" in value:
        out["batchName"] = value["batch_name"]
    out["requestId"] = value["request_id"]
    if "tags" in value:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.serialize_json(value["tags"])
    import aws_sdk_omics.types.default_run_setting

    out["defaultRunSetting"] = aws_sdk_omics.types.default_run_setting.serialize_json(
        value["default_run_setting"]
    )
    import aws_sdk_omics.types.batch_run_settings

    out["batchRunSettings"] = aws_sdk_omics.types.batch_run_settings.serialize_json(
        value["batch_run_settings"]
    )
    return out


def deserialize_json(data: dict) -> StartRunBatchRequest:
    out: StartRunBatchRequest = {}  # type: ignore[typeddict-item]
    if "batchName" in data:
        out["batch_name"] = data["batchName"]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    else:
        raise DeserializationError("StartRunBatchRequest.request_id required")
    if "tags" in data:
        import aws_sdk_omics.types.tag_map

        out["tags"] = aws_sdk_omics.types.tag_map.deserialize_json(data["tags"])
    if "defaultRunSetting" in data:
        import aws_sdk_omics.types.default_run_setting

        out["default_run_setting"] = (
            aws_sdk_omics.types.default_run_setting.deserialize_json(
                data["defaultRunSetting"]
            )
        )
    else:
        raise DeserializationError("StartRunBatchRequest.default_run_setting required")
    if "batchRunSettings" in data:
        import aws_sdk_omics.types.batch_run_settings

        out["batch_run_settings"] = (
            aws_sdk_omics.types.batch_run_settings.deserialize_json(
                data["batchRunSettings"]
            )
        )
    else:
        raise DeserializationError("StartRunBatchRequest.batch_run_settings required")
    return out
