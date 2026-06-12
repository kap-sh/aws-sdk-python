"""Generated from Smithy shape ``com.amazonaws.emr#AddInstanceFleetInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_fleet_config
    import aws_sdk_emr.types.xml_string_max_len256


class AddInstanceFleetInput(TypedDict):
    cluster_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The unique identifier of the cluster.</p>"""
    instance_fleet: NotRequired[
        "aws_sdk_emr.types.instance_fleet_config.InstanceFleetConfig"
    ]
    """<p>Specifies the configuration of the instance fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddInstanceFleetInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "instance_fleet" in value:
        import aws_sdk_emr.types.instance_fleet_config

        out["InstanceFleet"] = (
            aws_sdk_emr.types.instance_fleet_config.serialize_aws_json_1_1(
                value["instance_fleet"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddInstanceFleetInput:
    out: AddInstanceFleetInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "InstanceFleet" in data:
        import aws_sdk_emr.types.instance_fleet_config

        out["instance_fleet"] = (
            aws_sdk_emr.types.instance_fleet_config.deserialize_aws_json_1_1(
                data["InstanceFleet"]
            )
        )
    return out
