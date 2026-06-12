"""Generated from Smithy shape ``com.amazonaws.deadline#TaskRunManifestPropertiesListResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.task_run_manifest_properties_response

TaskRunManifestPropertiesListResponse: TypeAlias = list[
    "aws_sdk_deadline.types.task_run_manifest_properties_response.TaskRunManifestPropertiesResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskRunManifestPropertiesListResponse) -> list:
    import aws_sdk_deadline.types.task_run_manifest_properties_response

    out: list = []
    for item in value:
        out.append(
            aws_sdk_deadline.types.task_run_manifest_properties_response.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TaskRunManifestPropertiesListResponse:
    import aws_sdk_deadline.types.task_run_manifest_properties_response

    out: TaskRunManifestPropertiesListResponse = []
    for item in data:
        out.append(
            aws_sdk_deadline.types.task_run_manifest_properties_response.deserialize_json(
                item
            )
        )
    return out
