"""Generated from Smithy shape ``com.amazonaws.ses#GetSendStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.send_data_point_list


class GetSendStatisticsResponse(TypedDict, closed=True):
    send_data_points: NotRequired[
        "capo_ses.types.send_data_point_list.SendDataPointList"
    ]
    """<p>A list of data points, each of which represents 15 minutes of activity.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSendStatisticsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "send_data_points" in value:
        import capo_ses.types.send_data_point_list

        capo_ses.types.send_data_point_list.serialize_query(
            value["send_data_points"], pairs, f"{key_prefix}SendDataPoints"
        )


def deserialize_query(el: Element) -> GetSendStatisticsResponse:
    out: GetSendStatisticsResponse = {}  # type: ignore[typeddict-item]
    child_send_data_points = el.find("SendDataPoints")
    if child_send_data_points is not None:
        import capo_ses.types.send_data_point_list

        out["send_data_points"] = capo_ses.types.send_data_point_list.deserialize_query(
            child_send_data_points
        )
    return out
