"""Generated from Smithy shape ``com.amazonaws.neptunedata#ManageSparqlStatisticsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptunedata.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.refresh_statistics_id_map


class ManageSparqlStatisticsOutput(TypedDict):
    status: "str"
    """<p>The HTTP return code of the request. If the request succeeded, the code is 200.</p>"""
    payload: NotRequired[
        "aws_sdk_neptunedata.types.refresh_statistics_id_map.RefreshStatisticsIdMap"
    ]
    """<p>This is only returned for refresh mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManageSparqlStatisticsOutput) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "payload" in value:
        import aws_sdk_neptunedata.types.refresh_statistics_id_map

        out["payload"] = (
            aws_sdk_neptunedata.types.refresh_statistics_id_map.serialize_json(
                value["payload"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManageSparqlStatisticsOutput:
    out: ManageSparqlStatisticsOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ManageSparqlStatisticsOutput.status required")
    if "payload" in data:
        import aws_sdk_neptunedata.types.refresh_statistics_id_map

        out["payload"] = (
            aws_sdk_neptunedata.types.refresh_statistics_id_map.deserialize_json(
                data["payload"]
            )
        )
    return out
