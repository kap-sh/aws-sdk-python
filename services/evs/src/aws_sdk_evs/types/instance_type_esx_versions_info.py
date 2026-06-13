"""Generated from Smithy shape ``com.amazonaws.evs#InstanceTypeEsxVersionsInfo``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_evs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_evs.types.esx_version_list
    import aws_sdk_evs.types.instance_type


class InstanceTypeEsxVersionsInfo(TypedDict):
    instance_type: "aws_sdk_evs.types.instance_type.InstanceType"
    """<p>The EC2 instance type.</p>"""
    esx_versions: "aws_sdk_evs.types.esx_version_list.EsxVersionList"
    """<p>The list of ESX versions offered for this instance type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceTypeEsxVersionsInfo) -> dict:
    out: dict = {}
    import aws_sdk_evs.types.instance_type

    out["instanceType"] = aws_sdk_evs.types.instance_type.serialize_aws_json_1_0(
        value["instance_type"]
    )
    import aws_sdk_evs.types.esx_version_list

    out["esxVersions"] = aws_sdk_evs.types.esx_version_list.serialize_aws_json_1_0(
        value["esx_versions"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceTypeEsxVersionsInfo:
    out: InstanceTypeEsxVersionsInfo = {}  # type: ignore[typeddict-item]
    if "instanceType" in data:
        import aws_sdk_evs.types.instance_type

        out["instance_type"] = aws_sdk_evs.types.instance_type.deserialize_aws_json_1_0(
            data["instanceType"]
        )
    else:
        raise DeserializationError("InstanceTypeEsxVersionsInfo.instance_type required")
    if "esxVersions" in data:
        import aws_sdk_evs.types.esx_version_list

        out["esx_versions"] = (
            aws_sdk_evs.types.esx_version_list.deserialize_aws_json_1_0(
                data["esxVersions"]
            )
        )
    else:
        raise DeserializationError("InstanceTypeEsxVersionsInfo.esx_versions required")
    return out
