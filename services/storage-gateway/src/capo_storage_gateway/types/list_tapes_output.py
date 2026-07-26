"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListTapesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.marker
    import capo_storage_gateway.types.tape_infos


class ListTapesOutput(TypedDict, closed=True):
    tape_infos: NotRequired["capo_storage_gateway.types.tape_infos.TapeInfos"]
    marker: NotRequired["capo_storage_gateway.types.marker.Marker"]
    """<p>A string that indicates the position at which to begin returning the next list of tapes. Use the marker in your next request to continue pagination of tapes. If there are no more tapes to list, this element does not appear in the response body.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTapesOutput) -> dict:
    out: dict = {}
    if "tape_infos" in value:
        import capo_storage_gateway.types.tape_infos

        out["TapeInfos"] = capo_storage_gateway.types.tape_infos.serialize_aws_json_1_1(
            value["tape_infos"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTapesOutput:
    out: ListTapesOutput = {}  # type: ignore[typeddict-item]
    if "TapeInfos" in data:
        import capo_storage_gateway.types.tape_infos

        out["tape_infos"] = (
            capo_storage_gateway.types.tape_infos.deserialize_aws_json_1_1(
                data["TapeInfos"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
