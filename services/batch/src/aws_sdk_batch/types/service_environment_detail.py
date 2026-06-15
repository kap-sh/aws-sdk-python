"""Generated from Smithy shape ``com.amazonaws.batch#ServiceEnvironmentDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.capacity_limits
    import aws_sdk_batch.types.service_environment_state
    import aws_sdk_batch.types.service_environment_status
    import aws_sdk_batch.types.service_environment_type
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.tagris_tags_map


class ServiceEnvironmentDetail(TypedDict):
    service_environment_name: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name of the service environment.</p>"""
    service_environment_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the service environment.</p>"""
    service_environment_type: NotRequired[
        "aws_sdk_batch.types.service_environment_type.ServiceEnvironmentType"
    ]
    """<p>The type of service environment. For SageMaker Training jobs, this value is <code>SAGEMAKER_TRAINING</code>.</p>"""
    state: NotRequired[
        "aws_sdk_batch.types.service_environment_state.ServiceEnvironmentState"
    ]
    """<p>The state of the service environment. Valid values are <code>ENABLED</code> and <code>DISABLED</code>.</p>"""
    status: NotRequired[
        "aws_sdk_batch.types.service_environment_status.ServiceEnvironmentStatus"
    ]
    """<p>The current status of the service environment.</p>"""
    capacity_limits: NotRequired["aws_sdk_batch.types.capacity_limits.CapacityLimits"]
    """<p>The capacity limits for the service environment. This defines the maximum resources that can be used by service jobs in this environment.</p>"""
    tags: NotRequired["aws_sdk_batch.types.tagris_tags_map.TagrisTagsMap"]
    r"""<p>The tags associated with the service environment. Each tag consists of a key and an optional value. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html\">Tagging your Batch resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEnvironmentDetail) -> dict:
    out: dict = {}
    if "service_environment_name" in value:
        out["serviceEnvironmentName"] = value["service_environment_name"]
    if "service_environment_arn" in value:
        out["serviceEnvironmentArn"] = value["service_environment_arn"]
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
    if "status" in value:
        import aws_sdk_batch.types.service_environment_status

        out["status"] = aws_sdk_batch.types.service_environment_status.serialize_json(
            value["status"]
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


def deserialize_json(data: dict) -> ServiceEnvironmentDetail:
    out: ServiceEnvironmentDetail = {}  # type: ignore[typeddict-item]
    if "serviceEnvironmentName" in data:
        out["service_environment_name"] = data["serviceEnvironmentName"]
    if "serviceEnvironmentArn" in data:
        out["service_environment_arn"] = data["serviceEnvironmentArn"]
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
    if "status" in data:
        import aws_sdk_batch.types.service_environment_status

        out["status"] = aws_sdk_batch.types.service_environment_status.deserialize_json(
            data["status"]
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
