"""Generated from Smithy shape ``com.amazonaws.neptunedata#DeletePropertygraphStatisticsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.delete_statistics_value_map


class DeletePropertygraphStatisticsOutput(TypedDict, closed=True):
    status_code: NotRequired["int"]
    """<p>The HTTP response code: 200 if the delete was successful, or 204 if there were no statistics to delete.</p>"""
    status: NotRequired["str"]
    """<p>The cancel status.</p>"""
    payload: NotRequired[
        "aws_sdk_neptunedata.types.delete_statistics_value_map.DeleteStatisticsValueMap"
    ]
    """<p>The deletion payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePropertygraphStatisticsOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "payload" in value:
        import aws_sdk_neptunedata.types.delete_statistics_value_map

        out["payload"] = (
            aws_sdk_neptunedata.types.delete_statistics_value_map.serialize_json(
                value["payload"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeletePropertygraphStatisticsOutput:
    out: DeletePropertygraphStatisticsOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "payload" in data:
        import aws_sdk_neptunedata.types.delete_statistics_value_map

        out["payload"] = (
            aws_sdk_neptunedata.types.delete_statistics_value_map.deserialize_json(
                data["payload"]
            )
        )
    return out
