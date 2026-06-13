"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ReportGenerationResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.report_generation_result

ReportGenerationResultList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.report_generation_result.ReportGenerationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReportGenerationResultList) -> list:
    import aws_sdk_resiliencehubv2.types.report_generation_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehubv2.types.report_generation_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReportGenerationResultList:
    import aws_sdk_resiliencehubv2.types.report_generation_result

    out: ReportGenerationResultList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehubv2.types.report_generation_result.deserialize_json(
                item
            )
        )
    return out
