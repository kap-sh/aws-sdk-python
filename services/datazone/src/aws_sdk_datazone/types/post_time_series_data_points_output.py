"""Generated from Smithy shape ``com.amazonaws.datazone#PostTimeSeriesDataPointsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.entity_id
    import aws_sdk_datazone.types.time_series_data_point_form_output_list
    import aws_sdk_datazone.types.time_series_entity_type


class PostTimeSeriesDataPointsOutput(TypedDict):
    domain_id: NotRequired["aws_sdk_datazone.types.domain_id.DomainId"]
    """<p>The ID of the Amazon DataZone domain in which you want to post time series data points.</p>"""
    entity_id: NotRequired["aws_sdk_datazone.types.entity_id.EntityId"]
    """<p>The ID of the asset for which you want to post time series data points.</p>"""
    entity_type: NotRequired[
        "aws_sdk_datazone.types.time_series_entity_type.TimeSeriesEntityType"
    ]
    """<p>The type of the asset for which you want to post data points.</p>"""
    forms: NotRequired[
        "aws_sdk_datazone.types.time_series_data_point_form_output_list.TimeSeriesDataPointFormOutputList"
    ]
    """<p>The forms that contain the data points that you have posted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostTimeSeriesDataPointsOutput) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "entity_type" in value:
        import aws_sdk_datazone.types.time_series_entity_type

        out["entityType"] = (
            aws_sdk_datazone.types.time_series_entity_type.serialize_json(
                value["entity_type"]
            )
        )
    if "forms" in value:
        import aws_sdk_datazone.types.time_series_data_point_form_output_list

        out["forms"] = (
            aws_sdk_datazone.types.time_series_data_point_form_output_list.serialize_json(
                value["forms"]
            )
        )
    return out


def deserialize_json(data: dict) -> PostTimeSeriesDataPointsOutput:
    out: PostTimeSeriesDataPointsOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    if "entityType" in data:
        import aws_sdk_datazone.types.time_series_entity_type

        out["entity_type"] = (
            aws_sdk_datazone.types.time_series_entity_type.deserialize_json(
                data["entityType"]
            )
        )
    if "forms" in data:
        import aws_sdk_datazone.types.time_series_data_point_form_output_list

        out["forms"] = (
            aws_sdk_datazone.types.time_series_data_point_form_output_list.deserialize_json(
                data["forms"]
            )
        )
    return out
