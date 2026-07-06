"""Generated from Smithy shape ``com.amazonaws.datazone#PostTimeSeriesDataPointsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.entity_identifier
    import aws_sdk_datazone.types.time_series_data_point_form_input_list
    import aws_sdk_datazone.types.time_series_entity_type


class PostTimeSeriesDataPointsInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which you want to post time series data points.</p>"""
    entity_identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier"
    """<p>The ID of the asset for which you want to post time series data points.</p>"""
    entity_type: "aws_sdk_datazone.types.time_series_entity_type.TimeSeriesEntityType"
    """<p>The type of the asset for which you want to post data points.</p>"""
    forms: "aws_sdk_datazone.types.time_series_data_point_form_input_list.TimeSeriesDataPointFormInputList"
    """<p>The forms that contain the data points that you want to post.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostTimeSeriesDataPointsInput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.time_series_data_point_form_input_list

    out["forms"] = (
        aws_sdk_datazone.types.time_series_data_point_form_input_list.serialize_json(
            value["forms"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PostTimeSeriesDataPointsInput:
    out: PostTimeSeriesDataPointsInput = {}  # type: ignore[typeddict-item]
    if "forms" in data:
        import aws_sdk_datazone.types.time_series_data_point_form_input_list

        out["forms"] = (
            aws_sdk_datazone.types.time_series_data_point_form_input_list.deserialize_json(
                data["forms"]
            )
        )
    else:
        raise DeserializationError("PostTimeSeriesDataPointsInput.forms required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
