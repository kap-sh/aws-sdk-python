"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#WorkerConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.__timestamp_iso8601
    import capo_kafkaconnect.types.worker_configuration_revision_summary
    import capo_kafkaconnect.types.worker_configuration_state


class WorkerConfigurationSummary(TypedDict, closed=True):
    creation_time: NotRequired[
        "capo_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time that a worker configuration was created.</p>"""
    description: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The description of a worker configuration.</p>"""
    latest_revision: NotRequired[
        "capo_kafkaconnect.types.worker_configuration_revision_summary.WorkerConfigurationRevisionSummary"
    ]
    """<p>The latest revision of a worker configuration.</p>"""
    name: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The name of the worker configuration.</p>"""
    worker_configuration_arn: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the worker configuration.</p>"""
    worker_configuration_state: NotRequired[
        "capo_kafkaconnect.types.worker_configuration_state.WorkerConfigurationState"
    ]
    """<p>The state of the worker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerConfigurationSummary) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creationTime"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.serialize_json(
                value["creation_time"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "latest_revision" in value:
        import capo_kafkaconnect.types.worker_configuration_revision_summary

        out["latestRevision"] = (
            capo_kafkaconnect.types.worker_configuration_revision_summary.serialize_json(
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


def deserialize_json(data: dict) -> WorkerConfigurationSummary:
    out: WorkerConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "creationTime" in data:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creation_time"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["creationTime"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "latestRevision" in data:
        import capo_kafkaconnect.types.worker_configuration_revision_summary

        out["latest_revision"] = (
            capo_kafkaconnect.types.worker_configuration_revision_summary.deserialize_json(
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
