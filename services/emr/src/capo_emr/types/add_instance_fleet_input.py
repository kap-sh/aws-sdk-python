"""Generated from Smithy shape ``com.amazonaws.emr#AddInstanceFleetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.instance_fleet_config
    import capo_emr.types.xml_string_max_len256


class AddInstanceFleetInput(TypedDict, closed=True):
    cluster_id: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The unique identifier of the cluster.</p>"""
    instance_fleet: NotRequired[
        "capo_emr.types.instance_fleet_config.InstanceFleetConfig"
    ]
    """<p>Specifies the configuration of the instance fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddInstanceFleetInput) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "instance_fleet" in value:
        import capo_emr.types.instance_fleet_config

        out["InstanceFleet"] = (
            capo_emr.types.instance_fleet_config.serialize_aws_json_1_1(
                value["instance_fleet"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddInstanceFleetInput:
    out: AddInstanceFleetInput = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "InstanceFleet" in data:
        import capo_emr.types.instance_fleet_config

        out["instance_fleet"] = (
            capo_emr.types.instance_fleet_config.deserialize_aws_json_1_1(
                data["InstanceFleet"]
            )
        )
    return out
