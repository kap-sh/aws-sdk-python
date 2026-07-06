"""Generated from Smithy shape ``com.amazonaws.directconnect#Locations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.location_list


class Locations(TypedDict, closed=True):
    locations: NotRequired["aws_sdk_direct_connect.types.location_list.LocationList"]
    """<p>The locations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Locations) -> dict:
    out: dict = {}
    if "locations" in value:
        import aws_sdk_direct_connect.types.location_list

        out["locations"] = (
            aws_sdk_direct_connect.types.location_list.serialize_aws_json_1_1(
                value["locations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Locations:
    out: Locations = {}  # type: ignore[typeddict-item]
    if "locations" in data:
        import aws_sdk_direct_connect.types.location_list

        out["locations"] = (
            aws_sdk_direct_connect.types.location_list.deserialize_aws_json_1_1(
                data["locations"]
            )
        )
    return out
