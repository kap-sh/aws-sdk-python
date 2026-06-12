"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlInsightsMetadataByAssessment``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_insights_metadata_by_assessment_item

ControlInsightsMetadataByAssessment: TypeAlias = list[
    "aws_sdk_auditmanager.types.control_insights_metadata_by_assessment_item.ControlInsightsMetadataByAssessmentItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlInsightsMetadataByAssessment) -> list:
    import aws_sdk_auditmanager.types.control_insights_metadata_by_assessment_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_auditmanager.types.control_insights_metadata_by_assessment_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ControlInsightsMetadataByAssessment:
    import aws_sdk_auditmanager.types.control_insights_metadata_by_assessment_item

    out: ControlInsightsMetadataByAssessment = []
    for item in data:
        out.append(
            aws_sdk_auditmanager.types.control_insights_metadata_by_assessment_item.deserialize_json(
                item
            )
        )
    return out
