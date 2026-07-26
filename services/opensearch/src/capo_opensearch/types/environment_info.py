"""Generated from Smithy shape ``com.amazonaws.opensearch#EnvironmentInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.availability_zone_info_list


class EnvironmentInfo(TypedDict, closed=True):
    availability_zone_information: NotRequired[
        "capo_opensearch.types.availability_zone_info_list.AvailabilityZoneInfoList"
    ]
    """<p> A list of <code>AvailabilityZoneInfo</code> for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentInfo) -> dict:
    out: dict = {}
    if "availability_zone_information" in value:
        import capo_opensearch.types.availability_zone_info_list

        out["AvailabilityZoneInformation"] = (
            capo_opensearch.types.availability_zone_info_list.serialize_json(
                value["availability_zone_information"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnvironmentInfo:
    out: EnvironmentInfo = {}  # type: ignore[typeddict-item]
    if "AvailabilityZoneInformation" in data:
        import capo_opensearch.types.availability_zone_info_list

        out["availability_zone_information"] = (
            capo_opensearch.types.availability_zone_info_list.deserialize_json(
                data["AvailabilityZoneInformation"]
            )
        )
    return out
