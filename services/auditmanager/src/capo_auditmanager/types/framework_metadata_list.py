"""Generated from Smithy shape ``com.amazonaws.auditmanager#FrameworkMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_framework_metadata

FrameworkMetadataList: TypeAlias = list[
    "capo_auditmanager.types.assessment_framework_metadata.AssessmentFrameworkMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: FrameworkMetadataList) -> list:
    import capo_auditmanager.types.assessment_framework_metadata

    out: list = []
    for item in value:
        out.append(
            capo_auditmanager.types.assessment_framework_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FrameworkMetadataList:
    import capo_auditmanager.types.assessment_framework_metadata

    out: FrameworkMetadataList = []
    for item in data:
        out.append(
            capo_auditmanager.types.assessment_framework_metadata.deserialize_json(item)
        )
    return out
