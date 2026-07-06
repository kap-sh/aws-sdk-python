"""Generated from Smithy shape ``com.amazonaws.batch#CreateServiceEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.capacity_limits
    import aws_sdk_batch.types.service_environment_state
    import aws_sdk_batch.types.service_environment_type
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.tagris_tags_map


class CreateServiceEnvironmentRequest(TypedDict, closed=True):
    service_environment_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name for the service environment. It can be up to 128 characters long and can contain letters, numbers, hyphens (-), and underscores (_).</p>"""
    service_environment_type: NotRequired[
        "aws_sdk_batch.types.service_environment_type.ServiceEnvironmentType"
    ]
    """<p>The type of service environment. For SageMaker Training jobs, specify <code>SAGEMAKER_TRAINING</code>.</p>"""
    state: NotRequired[
        "aws_sdk_batch.types.service_environment_state.ServiceEnvironmentState"
    ]
    """<p>The state of the service environment. Valid values are <code>ENABLED</code> and <code>DISABLED</code>. The default value is <code>ENABLED</code>.</p>"""
    capacity_limits: NotRequired["aws_sdk_batch.types.capacity_limits.CapacityLimits"]
    """<p>The capacity limits for the service environment. The number of instances a job consumes is the total number of instances requested in the submit training job request resource configuration.</p>"""
    tags: NotRequired["aws_sdk_batch.types.tagris_tags_map.TagrisTagsMap"]
    r"""<p>The tags that you apply to the service environment to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html\">Tagging your Batch resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceEnvironmentRequest) -> dict:
    out: dict = {}
    if "service_environment_name" in value:
        out["serviceEnvironmentName"] = value["service_environment_name"]
    if "service_environment_type" in value:
        import aws_sdk_batch.types.service_environment_type

        out["serviceEnvironmentType"] = (
            aws_sdk_batch.types.service_environment_type.serialize_json(
                value["service_environment_type"]
            )
        )
    if "state" in value:
        import aws_sdk_batch.types.service_environment_state

        out["state"] = aws_sdk_batch.types.service_environment_state.serialize_json(
            value["state"]
        )
    if "capacity_limits" in value:
        import aws_sdk_batch.types.capacity_limits

        out["capacityLimits"] = aws_sdk_batch.types.capacity_limits.serialize_json(
            value["capacity_limits"]
        )
    if "tags" in value:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateServiceEnvironmentRequest:
    out: CreateServiceEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "serviceEnvironmentName" in data:
        out["service_environment_name"] = data["serviceEnvironmentName"]
    if "serviceEnvironmentType" in data:
        import aws_sdk_batch.types.service_environment_type

        out["service_environment_type"] = (
            aws_sdk_batch.types.service_environment_type.deserialize_json(
                data["serviceEnvironmentType"]
            )
        )
    if "state" in data:
        import aws_sdk_batch.types.service_environment_state

        out["state"] = aws_sdk_batch.types.service_environment_state.deserialize_json(
            data["state"]
        )
    if "capacityLimits" in data:
        import aws_sdk_batch.types.capacity_limits

        out["capacity_limits"] = aws_sdk_batch.types.capacity_limits.deserialize_json(
            data["capacityLimits"]
        )
    if "tags" in data:
        import aws_sdk_batch.types.tagris_tags_map

        out["tags"] = aws_sdk_batch.types.tagris_tags_map.deserialize_json(data["tags"])
    return out
