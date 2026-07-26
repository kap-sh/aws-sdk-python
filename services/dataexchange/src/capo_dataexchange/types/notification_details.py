"""Generated from Smithy shape ``com.amazonaws.dataexchange#NotificationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.data_update_request_details
    import capo_dataexchange.types.deprecation_request_details
    import capo_dataexchange.types.schema_change_request_details


class NotificationDetails(TypedDict, closed=True):
    data_update: NotRequired[
        "capo_dataexchange.types.data_update_request_details.DataUpdateRequestDetails"
    ]
    """<p>Extra details specific to a data update type notification.</p>"""
    deprecation: NotRequired[
        "capo_dataexchange.types.deprecation_request_details.DeprecationRequestDetails"
    ]
    """<p>Extra details specific to a deprecation type notification.</p>"""
    schema_change: NotRequired[
        "capo_dataexchange.types.schema_change_request_details.SchemaChangeRequestDetails"
    ]
    """<p>Extra details specific to a schema change type notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationDetails) -> dict:
    out: dict = {}
    if "data_update" in value:
        import capo_dataexchange.types.data_update_request_details

        out["DataUpdate"] = (
            capo_dataexchange.types.data_update_request_details.serialize_json(
                value["data_update"]
            )
        )
    if "deprecation" in value:
        import capo_dataexchange.types.deprecation_request_details

        out["Deprecation"] = (
            capo_dataexchange.types.deprecation_request_details.serialize_json(
                value["deprecation"]
            )
        )
    if "schema_change" in value:
        import capo_dataexchange.types.schema_change_request_details

        out["SchemaChange"] = (
            capo_dataexchange.types.schema_change_request_details.serialize_json(
                value["schema_change"]
            )
        )
    return out


def deserialize_json(data: dict) -> NotificationDetails:
    out: NotificationDetails = {}  # type: ignore[typeddict-item]
    if "DataUpdate" in data:
        import capo_dataexchange.types.data_update_request_details

        out["data_update"] = (
            capo_dataexchange.types.data_update_request_details.deserialize_json(
                data["DataUpdate"]
            )
        )
    if "Deprecation" in data:
        import capo_dataexchange.types.deprecation_request_details

        out["deprecation"] = (
            capo_dataexchange.types.deprecation_request_details.deserialize_json(
                data["Deprecation"]
            )
        )
    if "SchemaChange" in data:
        import capo_dataexchange.types.schema_change_request_details

        out["schema_change"] = (
            capo_dataexchange.types.schema_change_request_details.deserialize_json(
                data["SchemaChange"]
            )
        )
    return out
