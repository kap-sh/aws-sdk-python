"""Generated from Smithy shape ``com.amazonaws.evs#HostInfoForCreate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_evs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_evs.types.dedicated_host_id
    import aws_sdk_evs.types.host_name
    import aws_sdk_evs.types.instance_type
    import aws_sdk_evs.types.key_name
    import aws_sdk_evs.types.placement_group_id


class HostInfoForCreate(TypedDict, closed=True):
    host_name: "aws_sdk_evs.types.host_name.HostName"
    """<p>The DNS hostname of the host. DNS hostnames for hosts must be unique across Amazon EVS environments and within VCF.</p>"""
    key_name: "aws_sdk_evs.types.key_name.KeyName"
    """<p>The name of the SSH key that is used to access the host.</p>"""
    instance_type: "aws_sdk_evs.types.instance_type.InstanceType"
    """<p>The EC2 instance type that represents the host.</p>"""
    placement_group_id: NotRequired[
        "aws_sdk_evs.types.placement_group_id.PlacementGroupId"
    ]
    """<p>The unique ID of the placement group where the host is placed.</p>"""
    dedicated_host_id: NotRequired[
        "aws_sdk_evs.types.dedicated_host_id.DedicatedHostId"
    ]
    """<p>The unique ID of the Amazon EC2 Dedicated Host.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HostInfoForCreate) -> dict:
    out: dict = {}
    out["hostName"] = value["host_name"]
    out["keyName"] = value["key_name"]
    import aws_sdk_evs.types.instance_type

    out["instanceType"] = aws_sdk_evs.types.instance_type.serialize_aws_json_1_0(
        value["instance_type"]
    )
    if "placement_group_id" in value:
        out["placementGroupId"] = value["placement_group_id"]
    if "dedicated_host_id" in value:
        out["dedicatedHostId"] = value["dedicated_host_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> HostInfoForCreate:
    out: HostInfoForCreate = {}  # type: ignore[typeddict-item]
    if "hostName" in data:
        out["host_name"] = data["hostName"]
    else:
        raise DeserializationError("HostInfoForCreate.host_name required")
    if "keyName" in data:
        out["key_name"] = data["keyName"]
    else:
        raise DeserializationError("HostInfoForCreate.key_name required")
    if "instanceType" in data:
        import aws_sdk_evs.types.instance_type

        out["instance_type"] = aws_sdk_evs.types.instance_type.deserialize_aws_json_1_0(
            data["instanceType"]
        )
    else:
        raise DeserializationError("HostInfoForCreate.instance_type required")
    if "placementGroupId" in data:
        out["placement_group_id"] = data["placementGroupId"]
    if "dedicatedHostId" in data:
        out["dedicated_host_id"] = data["dedicatedHostId"]
    return out
