"""Generated from Smithy shape ``com.amazonaws.neptunedata#DeleteSparqlStatisticsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.delete_statistics_value_map


class DeleteSparqlStatisticsOutput(TypedDict, closed=True):
    status_code: NotRequired["int"]
    """<p>The HTTP response code: 200 if the delete was successful, or 204 if there were no statistics to delete.</p>"""
    status: NotRequired["str"]
    """<p>The cancel status.</p>"""
    payload: NotRequired[
        "capo_neptunedata.types.delete_statistics_value_map.DeleteStatisticsValueMap"
    ]
    """<p>The deletion payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSparqlStatisticsOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "payload" in value:
        import capo_neptunedata.types.delete_statistics_value_map

        out["payload"] = (
            capo_neptunedata.types.delete_statistics_value_map.serialize_json(
                value["payload"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteSparqlStatisticsOutput:
    out: DeleteSparqlStatisticsOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "payload" in data:
        import capo_neptunedata.types.delete_statistics_value_map

        out["payload"] = (
            capo_neptunedata.types.delete_statistics_value_map.deserialize_json(
                data["payload"]
            )
        )
    return out
