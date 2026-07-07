"""Generated from Smithy shape ``com.amazonaws.snowball#SnowconeDeviceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snowball.types.wireless_connection


class SnowconeDeviceConfiguration(TypedDict, closed=True):
    wireless_connection: NotRequired[
        "aws_sdk_snowball.types.wireless_connection.WirelessConnection"
    ]
    """<p>Configures the wireless connection for the Snowball Edge device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowconeDeviceConfiguration) -> dict:
    out: dict = {}
    if "wireless_connection" in value:
        import aws_sdk_snowball.types.wireless_connection

        out["WirelessConnection"] = (
            aws_sdk_snowball.types.wireless_connection.serialize_aws_json_1_1(
                value["wireless_connection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnowconeDeviceConfiguration:
    out: SnowconeDeviceConfiguration = {}  # type: ignore[typeddict-item]
    if "WirelessConnection" in data:
        import aws_sdk_snowball.types.wireless_connection

        out["wireless_connection"] = (
            aws_sdk_snowball.types.wireless_connection.deserialize_aws_json_1_1(
                data["WirelessConnection"]
            )
        )
    return out
