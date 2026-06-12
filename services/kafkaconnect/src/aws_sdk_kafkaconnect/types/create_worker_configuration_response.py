"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CreateWorkerConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.__timestamp_iso8601
    import aws_sdk_kafkaconnect.types.worker_configuration_revision_summary
    import aws_sdk_kafkaconnect.types.worker_configuration_state


class CreateWorkerConfigurationResponse(TypedDict):
    creation_time: NotRequired[
        "aws_sdk_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time that the worker configuration was created.</p>"""
    latest_revision: NotRequired[
        "aws_sdk_kafkaconnect.types.worker_configuration_revision_summary.WorkerConfigurationRevisionSummary"
    ]
    """<p>The latest revision of the worker configuration.</p>"""
    name: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The name of the worker configuration.</p>"""
    worker_configuration_arn: NotRequired[
        "aws_sdk_kafkaconnect.types.__string.__string"
    ]
    """<p>The Amazon Resource Name (ARN) that Amazon assigned to the worker configuration.</p>"""
    worker_configuration_state: NotRequired[
        "aws_sdk_kafkaconnect.types.worker_configuration_state.WorkerConfigurationState"
    ]
    """<p>The state of the worker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkerConfigurationResponse) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import aws_sdk_kafkaconnect.types.__timestamp_iso8601

        out["creationTime"] = (
            aws_sdk_kafkaconnect.types.__timestamp_iso8601.serialize_json(
                value["creation_time"]
            )
        )
    if "latest_revision" in value:
        import aws_sdk_kafkaconnect.types.worker_configuration_revision_summary

        out["latestRevision"] = (
            aws_sdk_kafkaconnect.types.worker_configuration_revision_summary.serialize_json(
                value["latest_revision"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "worker_configuration_arn" in value:
        out["workerConfigurationArn"] = value["worker_configuration_arn"]
    if "worker_configuration_state" in value:
        out["workerConfigurationState"] = value["worker_configuration_state"]
    return out


def deserialize_json(data: dict) -> CreateWorkerConfigurationResponse:
    out: CreateWorkerConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "creationTime" in data:
        import aws_sdk_kafkaconnect.types.__timestamp_iso8601

        out["creation_time"] = (
            aws_sdk_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["creationTime"]
            )
        )
    if "latestRevision" in data:
        import aws_sdk_kafkaconnect.types.worker_configuration_revision_summary

        out["latest_revision"] = (
            aws_sdk_kafkaconnect.types.worker_configuration_revision_summary.deserialize_json(
                data["latestRevision"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "workerConfigurationArn" in data:
        out["worker_configuration_arn"] = data["workerConfigurationArn"]
    if "workerConfigurationState" in data:
        out["worker_configuration_state"] = data["workerConfigurationState"]
    return out
