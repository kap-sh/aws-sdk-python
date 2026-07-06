"""Generated from Smithy shape ``com.amazonaws.mgn#ListConnectorsRequestFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.connector_i_ds_filter


class ListConnectorsRequestFilters(TypedDict, closed=True):
    connector_i_ds: NotRequired[
        "aws_sdk_mgn.types.connector_i_ds_filter.ConnectorIDsFilter"
    ]
    """<p>List Connectors Request Filters connector IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsRequestFilters) -> dict:
    out: dict = {}
    if "connector_i_ds" in value:
        import aws_sdk_mgn.types.connector_i_ds_filter

        out["connectorIDs"] = aws_sdk_mgn.types.connector_i_ds_filter.serialize_json(
            value["connector_i_ds"]
        )
    return out


def deserialize_json(data: dict) -> ListConnectorsRequestFilters:
    out: ListConnectorsRequestFilters = {}  # type: ignore[typeddict-item]
    if "connectorIDs" in data:
        import aws_sdk_mgn.types.connector_i_ds_filter

        out["connector_i_ds"] = (
            aws_sdk_mgn.types.connector_i_ds_filter.deserialize_json(
                data["connectorIDs"]
            )
        )
    return out
