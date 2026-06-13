"""Generated from Smithy shape ``com.amazonaws.drs#SourceProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.cpus
    import aws_sdk_drs.types.disks
    import aws_sdk_drs.types.ec2_instance_type
    import aws_sdk_drs.types.identification_hints
    import aws_sdk_drs.types.iso8601_datetime_string
    import aws_sdk_drs.types.network_interfaces
    import aws_sdk_drs.types.os
    import aws_sdk_drs.types.positive_integer


class SourceProperties(TypedDict):
    last_updated_date_time: NotRequired[
        "aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The date and time the Source Properties were last updated on.</p>"""
    recommended_instance_type: NotRequired[
        "aws_sdk_drs.types.ec2_instance_type.EC2InstanceType"
    ]
    """<p>The recommended EC2 instance type that will be used when recovering the Source Server.</p>"""
    identification_hints: NotRequired[
        "aws_sdk_drs.types.identification_hints.IdentificationHints"
    ]
    """<p>Hints used to uniquely identify a machine.</p>"""
    network_interfaces: NotRequired[
        "aws_sdk_drs.types.network_interfaces.NetworkInterfaces"
    ]
    """<p>An array of network interfaces.</p>"""
    disks: NotRequired["aws_sdk_drs.types.disks.Disks"]
    """<p>An array of disks.</p>"""
    cpus: NotRequired["aws_sdk_drs.types.cpus.Cpus"]
    """<p>An array of CPUs.</p>"""
    ram_bytes: "aws_sdk_drs.types.positive_integer.PositiveInteger"
    """<p>The amount of RAM in bytes.</p>"""
    os: NotRequired["aws_sdk_drs.types.os.OS"]
    """<p>Operating system.</p>"""
    supports_nitro_instances: NotRequired["bool"]
    """<p>Are EC2 nitro instance types supported when recovering the Source Server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceProperties) -> dict:
    out: dict = {}
    if "last_updated_date_time" in value:
        out["lastUpdatedDateTime"] = value["last_updated_date_time"]
    if "recommended_instance_type" in value:
        out["recommendedInstanceType"] = value["recommended_instance_type"]
    if "identification_hints" in value:
        import aws_sdk_drs.types.identification_hints

        out["identificationHints"] = (
            aws_sdk_drs.types.identification_hints.serialize_json(
                value["identification_hints"]
            )
        )
    if "network_interfaces" in value:
        import aws_sdk_drs.types.network_interfaces

        out["networkInterfaces"] = aws_sdk_drs.types.network_interfaces.serialize_json(
            value["network_interfaces"]
        )
    if "disks" in value:
        import aws_sdk_drs.types.disks

        out["disks"] = aws_sdk_drs.types.disks.serialize_json(value["disks"])
    if "cpus" in value:
        import aws_sdk_drs.types.cpus

        out["cpus"] = aws_sdk_drs.types.cpus.serialize_json(value["cpus"])
    out["ramBytes"] = value.get("ram_bytes", 0)
    if "os" in value:
        import aws_sdk_drs.types.os

        out["os"] = aws_sdk_drs.types.os.serialize_json(value["os"])
    if "supports_nitro_instances" in value:
        out["supportsNitroInstances"] = value["supports_nitro_instances"]
    return out


def deserialize_json(data: dict) -> SourceProperties:
    out: SourceProperties = {}  # type: ignore[typeddict-item]
    if "lastUpdatedDateTime" in data:
        out["last_updated_date_time"] = data["lastUpdatedDateTime"]
    if "recommendedInstanceType" in data:
        out["recommended_instance_type"] = data["recommendedInstanceType"]
    if "identificationHints" in data:
        import aws_sdk_drs.types.identification_hints

        out["identification_hints"] = (
            aws_sdk_drs.types.identification_hints.deserialize_json(
                data["identificationHints"]
            )
        )
    if "networkInterfaces" in data:
        import aws_sdk_drs.types.network_interfaces

        out["network_interfaces"] = (
            aws_sdk_drs.types.network_interfaces.deserialize_json(
                data["networkInterfaces"]
            )
        )
    if "disks" in data:
        import aws_sdk_drs.types.disks

        out["disks"] = aws_sdk_drs.types.disks.deserialize_json(data["disks"])
    if "cpus" in data:
        import aws_sdk_drs.types.cpus

        out["cpus"] = aws_sdk_drs.types.cpus.deserialize_json(data["cpus"])
    if "ramBytes" in data:
        out["ram_bytes"] = data["ramBytes"]
    else:
        out["ram_bytes"] = 0
    if "os" in data:
        import aws_sdk_drs.types.os

        out["os"] = aws_sdk_drs.types.os.deserialize_json(data["os"])
    if "supportsNitroInstances" in data:
        out["supports_nitro_instances"] = data["supportsNitroInstances"]
    return out
