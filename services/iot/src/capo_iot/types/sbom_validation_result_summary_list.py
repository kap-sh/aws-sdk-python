"""Generated from Smithy shape ``com.amazonaws.iot#SbomValidationResultSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.sbom_validation_result_summary

SbomValidationResultSummaryList: TypeAlias = list[
    "capo_iot.types.sbom_validation_result_summary.SbomValidationResultSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SbomValidationResultSummaryList) -> list:
    import capo_iot.types.sbom_validation_result_summary

    out: list = []
    for item in value:
        out.append(capo_iot.types.sbom_validation_result_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SbomValidationResultSummaryList:
    import capo_iot.types.sbom_validation_result_summary

    out: SbomValidationResultSummaryList = []
    for item in data:
        out.append(capo_iot.types.sbom_validation_result_summary.deserialize_json(item))
    return out
