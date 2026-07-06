"""Generated from Smithy shape ``com.amazonaws.iot#ConnectivityFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.fleet_indexing_api_list


class ConnectivityFilter(TypedDict, closed=True):
    include_socket_information: NotRequired[
        "aws_sdk_iot.types.fleet_indexing_api_list.FleetIndexingApiList"
    ]
    """<p>A list of fleet indexing APIs for which to enable socket information retrieval. Currently, the only supported value is <code>GET_THING_CONNECTIVITY_DATA</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectivityFilter) -> dict:
    out: dict = {}
    if "include_socket_information" in value:
        import aws_sdk_iot.types.fleet_indexing_api_list

        out["includeSocketInformation"] = (
            aws_sdk_iot.types.fleet_indexing_api_list.serialize_json(
                value["include_socket_information"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectivityFilter:
    out: ConnectivityFilter = {}  # type: ignore[typeddict-item]
    if "includeSocketInformation" in data:
        import aws_sdk_iot.types.fleet_indexing_api_list

        out["include_socket_information"] = (
            aws_sdk_iot.types.fleet_indexing_api_list.deserialize_json(
                data["includeSocketInformation"]
            )
        )
    return out
