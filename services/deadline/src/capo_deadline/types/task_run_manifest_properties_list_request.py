"""Generated from Smithy shape ``com.amazonaws.deadline#TaskRunManifestPropertiesListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.task_run_manifest_properties_request

TaskRunManifestPropertiesListRequest: TypeAlias = list[
    "capo_deadline.types.task_run_manifest_properties_request.TaskRunManifestPropertiesRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskRunManifestPropertiesListRequest) -> list:
    import capo_deadline.types.task_run_manifest_properties_request

    out: list = []
    for item in value:
        out.append(
            capo_deadline.types.task_run_manifest_properties_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TaskRunManifestPropertiesListRequest:
    import capo_deadline.types.task_run_manifest_properties_request

    out: TaskRunManifestPropertiesListRequest = []
    for item in data:
        out.append(
            capo_deadline.types.task_run_manifest_properties_request.deserialize_json(
                item
            )
        )
    return out
