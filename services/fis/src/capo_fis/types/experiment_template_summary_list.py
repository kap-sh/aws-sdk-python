"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_summary

ExperimentTemplateSummaryList: TypeAlias = list[
    "capo_fis.types.experiment_template_summary.ExperimentTemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateSummaryList) -> list:
    import capo_fis.types.experiment_template_summary

    out: list = []
    for item in value:
        out.append(capo_fis.types.experiment_template_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExperimentTemplateSummaryList:
    import capo_fis.types.experiment_template_summary

    out: ExperimentTemplateSummaryList = []
    for item in data:
        out.append(capo_fis.types.experiment_template_summary.deserialize_json(item))
    return out
