"""Generated from Smithy shape ``com.amazonaws.lakeformation#StorageOptimizer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.message_string
    import aws_sdk_lakeformation.types.optimizer_type
    import aws_sdk_lakeformation.types.storage_optimizer_config


class StorageOptimizer(TypedDict):
    storage_optimizer_type: NotRequired[
        "aws_sdk_lakeformation.types.optimizer_type.OptimizerType"
    ]
    """<p>The specific type of storage optimizer. The supported value is <code>compaction</code>.</p>"""
    config: NotRequired[
        "aws_sdk_lakeformation.types.storage_optimizer_config.StorageOptimizerConfig"
    ]
    """<p>A map of the storage optimizer configuration. Currently contains only one key-value pair: <code>is_enabled</code> indicates true or false for acceleration.</p>"""
    error_message: NotRequired[
        "aws_sdk_lakeformation.types.message_string.MessageString"
    ]
    r"""<p>A message that contains information about any error (if present).</p> <p>When an acceleration result has an enabled status, the error message is empty.</p> <p>When an acceleration result has a disabled status, the message describes an error or simply indicates \"disabled by the user\".</p>"""
    warnings: NotRequired["aws_sdk_lakeformation.types.message_string.MessageString"]
    """<p>A message that contains information about any warnings (if present).</p>"""
    last_run_details: NotRequired[
        "aws_sdk_lakeformation.types.message_string.MessageString"
    ]
    """<p>When an acceleration result has an enabled status, contains the details of the last job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageOptimizer) -> dict:
    out: dict = {}
    if "storage_optimizer_type" in value:
        import aws_sdk_lakeformation.types.optimizer_type

        out["StorageOptimizerType"] = (
            aws_sdk_lakeformation.types.optimizer_type.serialize_json(
                value["storage_optimizer_type"]
            )
        )
    if "config" in value:
        import aws_sdk_lakeformation.types.storage_optimizer_config

        out["Config"] = (
            aws_sdk_lakeformation.types.storage_optimizer_config.serialize_json(
                value["config"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "warnings" in value:
        out["Warnings"] = value["warnings"]
    if "last_run_details" in value:
        out["LastRunDetails"] = value["last_run_details"]
    return out


def deserialize_json(data: dict) -> StorageOptimizer:
    out: StorageOptimizer = {}  # type: ignore[typeddict-item]
    if "StorageOptimizerType" in data:
        import aws_sdk_lakeformation.types.optimizer_type

        out["storage_optimizer_type"] = (
            aws_sdk_lakeformation.types.optimizer_type.deserialize_json(
                data["StorageOptimizerType"]
            )
        )
    if "Config" in data:
        import aws_sdk_lakeformation.types.storage_optimizer_config

        out["config"] = (
            aws_sdk_lakeformation.types.storage_optimizer_config.deserialize_json(
                data["Config"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "Warnings" in data:
        out["warnings"] = data["Warnings"]
    if "LastRunDetails" in data:
        out["last_run_details"] = data["LastRunDetails"]
    return out
