"""Generated from Smithy shape ``com.amazonaws.opensearch#EnvironmentInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.availability_zone_info_list


class EnvironmentInfo(TypedDict):
    availability_zone_information: NotRequired[
        "aws_sdk_opensearch.types.availability_zone_info_list.AvailabilityZoneInfoList"
    ]
    """<p> A list of <code>AvailabilityZoneInfo</code> for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentInfo) -> dict:
    out: dict = {}
    if "availability_zone_information" in value:
        import aws_sdk_opensearch.types.availability_zone_info_list

        out["AvailabilityZoneInformation"] = (
            aws_sdk_opensearch.types.availability_zone_info_list.serialize_json(
                value["availability_zone_information"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnvironmentInfo:
    out: EnvironmentInfo = {}  # type: ignore[typeddict-item]
    if "AvailabilityZoneInformation" in data:
        import aws_sdk_opensearch.types.availability_zone_info_list

        out["availability_zone_information"] = (
            aws_sdk_opensearch.types.availability_zone_info_list.deserialize_json(
                data["AvailabilityZoneInformation"]
            )
        )
    return out
