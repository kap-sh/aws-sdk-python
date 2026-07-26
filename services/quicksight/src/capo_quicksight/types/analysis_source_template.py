"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisSourceTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.data_set_reference_list


class AnalysisSourceTemplate(TypedDict, closed=True):
    data_set_references: (
        "capo_quicksight.types.data_set_reference_list.DataSetReferenceList"
    )
    """<p>The dataset references of the source template of an analysis.</p>"""
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the source template of an analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSourceTemplate) -> dict:
    out: dict = {}
    import capo_quicksight.types.data_set_reference_list

    out["DataSetReferences"] = (
        capo_quicksight.types.data_set_reference_list.serialize_json(
            value["data_set_references"]
        )
    )
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> AnalysisSourceTemplate:
    out: AnalysisSourceTemplate = {}  # type: ignore[typeddict-item]
    if "DataSetReferences" in data:
        import capo_quicksight.types.data_set_reference_list

        out["data_set_references"] = (
            capo_quicksight.types.data_set_reference_list.deserialize_json(
                data["DataSetReferences"]
            )
        )
    else:
        raise DeserializationError(
            "AnalysisSourceTemplate.data_set_references required"
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("AnalysisSourceTemplate.arn required")
    return out
