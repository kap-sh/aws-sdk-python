"""Generated from Smithy shape ``com.amazonaws.medialive#ListSignalMapsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_signal_map_summary
    import aws_sdk_medialive.types.__string_min1_max2048


class ListSignalMapsResponse(TypedDict):
    next_token: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """A token used to retrieve the next set of results in paginated list responses."""
    signal_maps: NotRequired[
        "aws_sdk_medialive.types.__list_of_signal_map_summary.__listOfSignalMapSummary"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListSignalMapsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "signal_maps" in value:
        import aws_sdk_medialive.types.__list_of_signal_map_summary

        out["signalMaps"] = (
            aws_sdk_medialive.types.__list_of_signal_map_summary.serialize_json(
                value["signal_maps"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListSignalMapsResponse:
    out: ListSignalMapsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "signalMaps" in data:
        import aws_sdk_medialive.types.__list_of_signal_map_summary

        out["signal_maps"] = (
            aws_sdk_medialive.types.__list_of_signal_map_summary.deserialize_json(
                data["signalMaps"]
            )
        )
    return out
