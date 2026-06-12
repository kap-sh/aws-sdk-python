"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentFrameworkShareRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_framework_share_request

AssessmentFrameworkShareRequestList: TypeAlias = list[
    "aws_sdk_auditmanager.types.assessment_framework_share_request.AssessmentFrameworkShareRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentFrameworkShareRequestList) -> list:
    import aws_sdk_auditmanager.types.assessment_framework_share_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_auditmanager.types.assessment_framework_share_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssessmentFrameworkShareRequestList:
    import aws_sdk_auditmanager.types.assessment_framework_share_request

    out: AssessmentFrameworkShareRequestList = []
    for item in data:
        out.append(
            aws_sdk_auditmanager.types.assessment_framework_share_request.deserialize_json(
                item
            )
        )
    return out
