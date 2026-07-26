"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.form_summary

FormSummaryList: TypeAlias = list[
    "capo_amplifyuibuilder.types.form_summary.FormSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FormSummaryList) -> list:
    import capo_amplifyuibuilder.types.form_summary

    out: list = []
    for item in value:
        out.append(capo_amplifyuibuilder.types.form_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FormSummaryList:
    import capo_amplifyuibuilder.types.form_summary

    out: FormSummaryList = []
    for item in data:
        out.append(capo_amplifyuibuilder.types.form_summary.deserialize_json(item))
    return out
