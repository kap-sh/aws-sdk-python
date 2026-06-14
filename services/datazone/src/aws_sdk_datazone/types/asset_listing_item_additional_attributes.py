"""Generated from Smithy shape ``com.amazonaws.datazone#AssetListingItemAdditionalAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.forms
    import aws_sdk_datazone.types.match_rationale
    import aws_sdk_datazone.types.time_series_data_point_summary_form_output_list


class AssetListingItemAdditionalAttributes(TypedDict):
    forms: NotRequired["aws_sdk_datazone.types.forms.Forms"]
    """<p>The metadata forms that form additional attributes of the metadata asset.</p>"""
    match_rationale: NotRequired[
        "aws_sdk_datazone.types.match_rationale.MatchRationale"
    ]
    """<p>List of rationales indicating why this item was matched by search.</p>"""
    latest_time_series_data_point_forms: NotRequired[
        "aws_sdk_datazone.types.time_series_data_point_summary_form_output_list.TimeSeriesDataPointSummaryFormOutputList"
    ]
    """<p>The latest time series data points forms included in the additional attributes of an asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetListingItemAdditionalAttributes) -> dict:
    out: dict = {}
    if "forms" in value:
        out["forms"] = value["forms"]
    if "match_rationale" in value:
        import aws_sdk_datazone.types.match_rationale

        out["matchRationale"] = aws_sdk_datazone.types.match_rationale.serialize_json(
            value["match_rationale"]
        )
    if "latest_time_series_data_point_forms" in value:
        import aws_sdk_datazone.types.time_series_data_point_summary_form_output_list

        out["latestTimeSeriesDataPointForms"] = (
            aws_sdk_datazone.types.time_series_data_point_summary_form_output_list.serialize_json(
                value["latest_time_series_data_point_forms"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetListingItemAdditionalAttributes:
    out: AssetListingItemAdditionalAttributes = {}  # type: ignore[typeddict-item]
    if "forms" in data:
        out["forms"] = data["forms"]
    if "matchRationale" in data:
        import aws_sdk_datazone.types.match_rationale

        out["match_rationale"] = (
            aws_sdk_datazone.types.match_rationale.deserialize_json(
                data["matchRationale"]
            )
        )
    if "latestTimeSeriesDataPointForms" in data:
        import aws_sdk_datazone.types.time_series_data_point_summary_form_output_list

        out["latest_time_series_data_point_forms"] = (
            aws_sdk_datazone.types.time_series_data_point_summary_form_output_list.deserialize_json(
                data["latestTimeSeriesDataPointForms"]
            )
        )
    return out
