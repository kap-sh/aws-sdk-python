"""Generated from Smithy shape ``com.amazonaws.quicksight#ContributionAnalysisDefault``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.contributor_dimension_list
    import aws_sdk_quicksight.types.field_id


class ContributionAnalysisDefault(TypedDict):
    measure_field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The measure field that is used in the contribution analysis.</p>"""
    contributor_dimensions: (
        "aws_sdk_quicksight.types.contributor_dimension_list.ContributorDimensionList"
    )
    """<p>The dimensions columns that are used in the contribution analysis, usually a list of <code>ColumnIdentifiers</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContributionAnalysisDefault) -> dict:
    out: dict = {}
    out["MeasureFieldId"] = value["measure_field_id"]
    import aws_sdk_quicksight.types.contributor_dimension_list

    out["ContributorDimensions"] = (
        aws_sdk_quicksight.types.contributor_dimension_list.serialize_json(
            value["contributor_dimensions"]
        )
    )
    return out


def deserialize_json(data: dict) -> ContributionAnalysisDefault:
    out: ContributionAnalysisDefault = {}  # type: ignore[typeddict-item]
    if "MeasureFieldId" in data:
        out["measure_field_id"] = data["MeasureFieldId"]
    else:
        raise DeserializationError(
            "ContributionAnalysisDefault.measure_field_id required"
        )
    if "ContributorDimensions" in data:
        import aws_sdk_quicksight.types.contributor_dimension_list

        out["contributor_dimensions"] = (
            aws_sdk_quicksight.types.contributor_dimension_list.deserialize_json(
                data["ContributorDimensions"]
            )
        )
    else:
        raise DeserializationError(
            "ContributionAnalysisDefault.contributor_dimensions required"
        )
    return out
