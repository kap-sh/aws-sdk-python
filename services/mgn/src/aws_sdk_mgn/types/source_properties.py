"""Generated from Smithy shape ``com.amazonaws.mgn#SourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.cpus
    import aws_sdk_mgn.types.disks
    import aws_sdk_mgn.types.ec2_instance_type
    import aws_sdk_mgn.types.identification_hints
    import aws_sdk_mgn.types.iso8601_datetime_string
    import aws_sdk_mgn.types.network_interfaces
    import aws_sdk_mgn.types.os
    import aws_sdk_mgn.types.positive_integer


class SourceProperties(TypedDict, closed=True):
    last_updated_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Source server last update date and time.</p>"""
    recommended_instance_type: NotRequired[
        "aws_sdk_mgn.types.ec2_instance_type.EC2InstanceType"
    ]
    """<p>Source server recommended instance type.</p>"""
    identification_hints: NotRequired[
        "aws_sdk_mgn.types.identification_hints.IdentificationHints"
    ]
    """<p>Source server identification hints.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_mgn.types.network_interfaces.NetworkInterfaces"
    ]
    """<p>Source server network interfaces.</p>"""
    disks: NotRequired["aws_sdk_mgn.types.disks.Disks"]
    """<p>Source Server disks.</p>"""
    cpus: NotRequired["aws_sdk_mgn.types.cpus.Cpus"]
    """<p>Source Server CPUs.</p>"""
    ram_bytes: "aws_sdk_mgn.types.positive_integer.PositiveInteger"
    """<p>Source server RAM in bytes.</p>"""
    os: NotRequired["aws_sdk_mgn.types.os.OS"]
    """<p>Source server OS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceProperties) -> dict:
    out: dict = {}
    if "last_updated_date_time" in value:
        out["lastUpdatedDateTime"] = value["last_updated_date_time"]
    if "recommended_instance_type" in value:
        out["recommendedInstanceType"] = value["recommended_instance_type"]
    if "identification_hints" in value:
        import aws_sdk_mgn.types.identification_hints

        out["identificationHints"] = (
            aws_sdk_mgn.types.identification_hints.serialize_json(
                value["identification_hints"]
            )
        )
    if "network_interfaces" in value:
        import aws_sdk_mgn.types.network_interfaces

        out["networkInterfaces"] = aws_sdk_mgn.types.network_interfaces.serialize_json(
            value["network_interfaces"]
        )
    if "disks" in value:
        import aws_sdk_mgn.types.disks

        out["disks"] = aws_sdk_mgn.types.disks.serialize_json(value["disks"])
    if "cpus" in value:
        import aws_sdk_mgn.types.cpus

        out["cpus"] = aws_sdk_mgn.types.cpus.serialize_json(value["cpus"])
    out["ramBytes"] = value.get("ram_bytes", 0)
    if "os" in value:
        import aws_sdk_mgn.types.os

        out["os"] = aws_sdk_mgn.types.os.serialize_json(value["os"])
    return out


def deserialize_json(data: dict) -> SourceProperties:
    out: SourceProperties = {}  # type: ignore[typeddict-item]
    if "lastUpdatedDateTime" in data:
        out["last_updated_date_time"] = data["lastUpdatedDateTime"]
    if "recommendedInstanceType" in data:
        out["recommended_instance_type"] = data["recommendedInstanceType"]
    if "identificationHints" in data:
        import aws_sdk_mgn.types.identification_hints

        out["identification_hints"] = (
            aws_sdk_mgn.types.identification_hints.deserialize_json(
                data["identificationHints"]
            )
        )
    if "networkInterfaces" in data:
        import aws_sdk_mgn.types.network_interfaces

        out["network_interfaces"] = (
            aws_sdk_mgn.types.network_interfaces.deserialize_json(
                data["networkInterfaces"]
            )
        )
    if "disks" in data:
        import aws_sdk_mgn.types.disks

        out["disks"] = aws_sdk_mgn.types.disks.deserialize_json(data["disks"])
    if "cpus" in data:
        import aws_sdk_mgn.types.cpus

        out["cpus"] = aws_sdk_mgn.types.cpus.deserialize_json(data["cpus"])
    if "ramBytes" in data:
        out["ram_bytes"] = data["ramBytes"]
    else:
        out["ram_bytes"] = 0
    if "os" in data:
        import aws_sdk_mgn.types.os

        out["os"] = aws_sdk_mgn.types.os.deserialize_json(data["os"])
    return out
