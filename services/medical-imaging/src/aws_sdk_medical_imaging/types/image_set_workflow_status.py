"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImageSetWorkflowStatus``."""

from typing import Literal, TypeAlias, cast

ImageSetWorkflowStatus: TypeAlias = Literal[
    "CREATED",
    "COPIED",
    "COPYING",
    "COPYING_WITH_READ_ONLY_ACCESS",
    "COPY_FAILED",
    "UPDATING",
    "UPDATING_FOR_STUDY_CONSISTENCY",
    "UPDATED",
    "UPDATE_FAILED",
    "DELETING",
    "DELETED",
    "IMPORTING",
    "IMPORTED",
    "IMPORT_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageSetWorkflowStatus) -> str:
    return value


def deserialize_json(data: str) -> ImageSetWorkflowStatus:
    return cast(ImageSetWorkflowStatus, data)
