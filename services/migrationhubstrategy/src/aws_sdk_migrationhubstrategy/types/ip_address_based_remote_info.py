"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#IPAddressBasedRemoteInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.auth_type
    import aws_sdk_migrationhubstrategy.types.os_type
    import aws_sdk_migrationhubstrategy.types.string


class IPAddressBasedRemoteInfo(TypedDict):
    ip_address_configuration_time_stamp: NotRequired[
        "aws_sdk_migrationhubstrategy.types.string.String"
    ]
    """<p>The time stamp of the configuration.</p>"""
    auth_type: NotRequired["aws_sdk_migrationhubstrategy.types.auth_type.AuthType"]
    """<p>The type of authorization.</p>"""
    os_type: NotRequired["aws_sdk_migrationhubstrategy.types.os_type.OSType"]
    """<p>The type of the operating system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IPAddressBasedRemoteInfo) -> dict:
    out: dict = {}
    if "ip_address_configuration_time_stamp" in value:
        out["ipAddressConfigurationTimeStamp"] = value[
            "ip_address_configuration_time_stamp"
        ]
    if "auth_type" in value:
        out["authType"] = value["auth_type"]
    if "os_type" in value:
        out["osType"] = value["os_type"]
    return out


def deserialize_json(data: dict) -> IPAddressBasedRemoteInfo:
    out: IPAddressBasedRemoteInfo = {}  # type: ignore[typeddict-item]
    if "ipAddressConfigurationTimeStamp" in data:
        out["ip_address_configuration_time_stamp"] = data[
            "ipAddressConfigurationTimeStamp"
        ]
    if "authType" in data:
        out["auth_type"] = data["authType"]
    if "osType" in data:
        out["os_type"] = data["osType"]
    return out
