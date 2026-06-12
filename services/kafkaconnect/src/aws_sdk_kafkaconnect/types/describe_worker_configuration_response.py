"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DescribeWorkerConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.__timestamp_iso8601
    import aws_sdk_kafkaconnect.types.worker_configuration_revision_description
    import aws_sdk_kafkaconnect.types.worker_configuration_state


class DescribeWorkerConfigurationResponse(TypedDict):
    creation_time: NotRequired[
        "aws_sdk_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time that the worker configuration was created.</p>"""
    description: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The description of the worker configuration.</p>"""
    latest_revision: NotRequired[
        "aws_sdk_kafkaconnect.types.worker_configuration_revision_description.WorkerConfigurationRevisionDescription"
    ]
    """<p>The latest revision of the custom configuration.</p>"""
    name: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The name of the worker configuration.</p>"""
    worker_configuration_arn: NotRequired[
        "aws_sdk_kafkaconnect.types.__string.__string"
    ]
    """<p>The Amazon Resource Name (ARN) of the custom configuration.</p>"""
    worker_configuration_state: NotRequired[
        "aws_sdk_kafkaconnect.types.worker_configuration_state.WorkerConfigurationState"
    ]
    """<p>The state of the worker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkerConfigurationResponse) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import aws_sdk_kafkaconnect.types.__timestamp_iso8601

        out["creationTime"] = (
            aws_sdk_kafkaconnect.types.__timestamp_iso8601.serialize_json(
                value["creation_time"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "latest_revision" in value:
        import aws_sdk_kafkaconnect.types.worker_configuration_revision_description

        out["latestRevision"] = (
            aws_sdk_kafkaconnect.types.worker_configuration_revision_description.serialize_json(
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


def deserialize_json(data: dict) -> DescribeWorkerConfigurationResponse:
    out: DescribeWorkerConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "creationTime" in data:
        import aws_sdk_kafkaconnect.types.__timestamp_iso8601

        out["creation_time"] = (
            aws_sdk_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["creationTime"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "latestRevision" in data:
        import aws_sdk_kafkaconnect.types.worker_configuration_revision_description

        out["latest_revision"] = (
            aws_sdk_kafkaconnect.types.worker_configuration_revision_description.deserialize_json(
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
