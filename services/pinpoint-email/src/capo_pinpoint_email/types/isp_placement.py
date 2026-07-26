"""Generated from Smithy shape ``com.amazonaws.pinpointemail#IspPlacement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.isp_name
    import capo_pinpoint_email.types.placement_statistics


class IspPlacement(TypedDict, closed=True):
    isp_name: NotRequired["capo_pinpoint_email.types.isp_name.IspName"]
    """<p>The name of the email provider that the inbox placement data applies to.</p>"""
    placement_statistics: NotRequired[
        "capo_pinpoint_email.types.placement_statistics.PlacementStatistics"
    ]
    """<p>An object that contains inbox placement metrics for a specific email provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IspPlacement) -> dict:
    out: dict = {}
    if "isp_name" in value:
        out["IspName"] = value["isp_name"]
    if "placement_statistics" in value:
        import capo_pinpoint_email.types.placement_statistics

        out["PlacementStatistics"] = (
            capo_pinpoint_email.types.placement_statistics.serialize_json(
                value["placement_statistics"]
            )
        )
    return out


def deserialize_json(data: dict) -> IspPlacement:
    out: IspPlacement = {}  # type: ignore[typeddict-item]
    if "IspName" in data:
        out["isp_name"] = data["IspName"]
    if "PlacementStatistics" in data:
        import capo_pinpoint_email.types.placement_statistics

        out["placement_statistics"] = (
            capo_pinpoint_email.types.placement_statistics.deserialize_json(
                data["PlacementStatistics"]
            )
        )
    return out
