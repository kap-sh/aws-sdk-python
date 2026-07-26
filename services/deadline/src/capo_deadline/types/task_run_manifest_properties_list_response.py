"""Generated from Smithy shape ``com.amazonaws.deadline#TaskRunManifestPropertiesListResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.task_run_manifest_properties_response

TaskRunManifestPropertiesListResponse: TypeAlias = list[
    "capo_deadline.types.task_run_manifest_properties_response.TaskRunManifestPropertiesResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskRunManifestPropertiesListResponse) -> list:
    import capo_deadline.types.task_run_manifest_properties_response

    out: list = []
    for item in value:
        out.append(
            capo_deadline.types.task_run_manifest_properties_response.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TaskRunManifestPropertiesListResponse:
    import capo_deadline.types.task_run_manifest_properties_response

    out: TaskRunManifestPropertiesListResponse = []
    for item in data:
        out.append(
            capo_deadline.types.task_run_manifest_properties_response.deserialize_json(
                item
            )
        )
    return out
