"""Generated from Smithy shape ``com.amazonaws.auditmanager#FrameworkMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_framework_metadata

FrameworkMetadataList: TypeAlias = list[
    "aws_sdk_auditmanager.types.assessment_framework_metadata.AssessmentFrameworkMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: FrameworkMetadataList) -> list:
    import aws_sdk_auditmanager.types.assessment_framework_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_auditmanager.types.assessment_framework_metadata.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FrameworkMetadataList:
    import aws_sdk_auditmanager.types.assessment_framework_metadata

    out: FrameworkMetadataList = []
    for item in data:
        out.append(
            aws_sdk_auditmanager.types.assessment_framework_metadata.deserialize_json(
                item
            )
        )
    return out
