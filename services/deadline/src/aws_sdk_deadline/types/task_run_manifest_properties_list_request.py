"""Generated from Smithy shape ``com.amazonaws.deadline#TaskRunManifestPropertiesListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.task_run_manifest_properties_request

TaskRunManifestPropertiesListRequest: TypeAlias = list[
    "aws_sdk_deadline.types.task_run_manifest_properties_request.TaskRunManifestPropertiesRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskRunManifestPropertiesListRequest) -> list:
    import aws_sdk_deadline.types.task_run_manifest_properties_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_deadline.types.task_run_manifest_properties_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TaskRunManifestPropertiesListRequest:
    import aws_sdk_deadline.types.task_run_manifest_properties_request

    out: TaskRunManifestPropertiesListRequest = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.task_run_manifest_properties_request.deserialize_json(
                item
            )
        )
    return out
