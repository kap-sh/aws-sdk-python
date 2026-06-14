"""Generated from Smithy shape ``com.amazonaws.datazone#AssetItemAdditionalAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.form_output_list
    import aws_sdk_datazone.types.match_rationale
    import aws_sdk_datazone.types.time_series_data_point_summary_form_output_list


class AssetItemAdditionalAttributes(TypedDict):
    forms_output: NotRequired["aws_sdk_datazone.types.form_output_list.FormOutputList"]
    """<p>The forms included in the additional attributes of an inventory asset.</p>"""
    read_only_forms_output: NotRequired[
        "aws_sdk_datazone.types.form_output_list.FormOutputList"
    ]
    """<p>The read-only forms included in the additional attributes of an inventory asset.</p>"""
    latest_time_series_data_point_forms_output: NotRequired[
        "aws_sdk_datazone.types.time_series_data_point_summary_form_output_list.TimeSeriesDataPointSummaryFormOutputList"
    ]
    """<p>The latest time series data points forms included in the additional attributes of an asset.</p>"""
    match_rationale: NotRequired[
        "aws_sdk_datazone.types.match_rationale.MatchRationale"
    ]
    """<p>List of rationales indicating why this item was matched by search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetItemAdditionalAttributes) -> dict:
    out: dict = {}
    if "forms_output" in value:
        import aws_sdk_datazone.types.form_output_list

        out["formsOutput"] = aws_sdk_datazone.types.form_output_list.serialize_json(
            value["forms_output"]
        )
    if "read_only_forms_output" in value:
        import aws_sdk_datazone.types.form_output_list

        out["readOnlyFormsOutput"] = (
            aws_sdk_datazone.types.form_output_list.serialize_json(
                value["read_only_forms_output"]
            )
        )
    if "latest_time_series_data_point_forms_output" in value:
        import aws_sdk_datazone.types.time_series_data_point_summary_form_output_list

        out["latestTimeSeriesDataPointFormsOutput"] = (
            aws_sdk_datazone.types.time_series_data_point_summary_form_output_list.serialize_json(
                value["latest_time_series_data_point_forms_output"]
            )
        )
    if "match_rationale" in value:
        import aws_sdk_datazone.types.match_rationale

        out["matchRationale"] = aws_sdk_datazone.types.match_rationale.serialize_json(
            value["match_rationale"]
        )
    return out


def deserialize_json(data: dict) -> AssetItemAdditionalAttributes:
    out: AssetItemAdditionalAttributes = {}  # type: ignore[typeddict-item]
    if "formsOutput" in data:
        import aws_sdk_datazone.types.form_output_list

        out["forms_output"] = aws_sdk_datazone.types.form_output_list.deserialize_json(
            data["formsOutput"]
        )
    if "readOnlyFormsOutput" in data:
        import aws_sdk_datazone.types.form_output_list

        out["read_only_forms_output"] = (
            aws_sdk_datazone.types.form_output_list.deserialize_json(
                data["readOnlyFormsOutput"]
            )
        )
    if "latestTimeSeriesDataPointFormsOutput" in data:
        import aws_sdk_datazone.types.time_series_data_point_summary_form_output_list

        out["latest_time_series_data_point_forms_output"] = (
            aws_sdk_datazone.types.time_series_data_point_summary_form_output_list.deserialize_json(
                data["latestTimeSeriesDataPointFormsOutput"]
            )
        )
    if "matchRationale" in data:
        import aws_sdk_datazone.types.match_rationale

        out["match_rationale"] = (
            aws_sdk_datazone.types.match_rationale.deserialize_json(
                data["matchRationale"]
            )
        )
    return out
