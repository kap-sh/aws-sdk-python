"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateSourceAnalysis``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.data_set_reference_list


class TemplateSourceAnalysis(TypedDict, closed=True):
    arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    data_set_references: (
        "aws_sdk_quicksight.types.data_set_reference_list.DataSetReferenceList"
    )
    """<p>A structure containing information about the dataset references used as placeholders in the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSourceAnalysis) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import aws_sdk_quicksight.types.data_set_reference_list

    out["DataSetReferences"] = (
        aws_sdk_quicksight.types.data_set_reference_list.serialize_json(
            value["data_set_references"]
        )
    )
    return out


def deserialize_json(data: dict) -> TemplateSourceAnalysis:
    out: TemplateSourceAnalysis = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("TemplateSourceAnalysis.arn required")
    if "DataSetReferences" in data:
        import aws_sdk_quicksight.types.data_set_reference_list

        out["data_set_references"] = (
            aws_sdk_quicksight.types.data_set_reference_list.deserialize_json(
                data["DataSetReferences"]
            )
        )
    else:
        raise DeserializationError(
            "TemplateSourceAnalysis.data_set_references required"
        )
    return out
