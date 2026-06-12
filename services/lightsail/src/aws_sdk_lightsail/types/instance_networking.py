"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceNetworking``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.instance_port_info_list
    import aws_sdk_lightsail.types.monthly_transfer


class InstanceNetworking(TypedDict):
    monthly_transfer: NotRequired[
        "aws_sdk_lightsail.types.monthly_transfer.MonthlyTransfer"
    ]
    """<p>The amount of data in GB allocated for monthly data transfers.</p>"""
    ports: NotRequired[
        "aws_sdk_lightsail.types.instance_port_info_list.InstancePortInfoList"
    ]
    """<p>An array of key-value pairs containing information about the ports on the instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceNetworking) -> dict:
    out: dict = {}
    if "monthly_transfer" in value:
        import aws_sdk_lightsail.types.monthly_transfer

        out["monthlyTransfer"] = (
            aws_sdk_lightsail.types.monthly_transfer.serialize_aws_json_1_1(
                value["monthly_transfer"]
            )
        )
    if "ports" in value:
        import aws_sdk_lightsail.types.instance_port_info_list

        out["ports"] = (
            aws_sdk_lightsail.types.instance_port_info_list.serialize_aws_json_1_1(
                value["ports"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceNetworking:
    out: InstanceNetworking = {}  # type: ignore[typeddict-item]
    if "monthlyTransfer" in data:
        import aws_sdk_lightsail.types.monthly_transfer

        out["monthly_transfer"] = (
            aws_sdk_lightsail.types.monthly_transfer.deserialize_aws_json_1_1(
                data["monthlyTransfer"]
            )
        )
    if "ports" in data:
        import aws_sdk_lightsail.types.instance_port_info_list

        out["ports"] = (
            aws_sdk_lightsail.types.instance_port_info_list.deserialize_aws_json_1_1(
                data["ports"]
            )
        )
    return out
