"""Generated from Smithy shape ``com.amazonaws.evs#GetVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_evs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_evs.types.instance_type_esx_versions_list
    import aws_sdk_evs.types.vcf_version_list


class GetVersionsResponse(TypedDict, closed=True):
    vcf_versions: "aws_sdk_evs.types.vcf_version_list.VcfVersionList"
    """<p>A list of VCF versions with their availability status, default ESX version, and instance types.</p>"""
    instance_type_esx_versions: (
        "aws_sdk_evs.types.instance_type_esx_versions_list.InstanceTypeEsxVersionsList"
    )
    """<p>A list of EC2 instance types and their available ESX versions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetVersionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_evs.types.vcf_version_list

    out["vcfVersions"] = aws_sdk_evs.types.vcf_version_list.serialize_aws_json_1_0(
        value["vcf_versions"]
    )
    import aws_sdk_evs.types.instance_type_esx_versions_list

    out["instanceTypeEsxVersions"] = (
        aws_sdk_evs.types.instance_type_esx_versions_list.serialize_aws_json_1_0(
            value["instance_type_esx_versions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetVersionsResponse:
    out: GetVersionsResponse = {}  # type: ignore[typeddict-item]
    if "vcfVersions" in data:
        import aws_sdk_evs.types.vcf_version_list

        out["vcf_versions"] = (
            aws_sdk_evs.types.vcf_version_list.deserialize_aws_json_1_0(
                data["vcfVersions"]
            )
        )
    else:
        raise DeserializationError("GetVersionsResponse.vcf_versions required")
    if "instanceTypeEsxVersions" in data:
        import aws_sdk_evs.types.instance_type_esx_versions_list

        out["instance_type_esx_versions"] = (
            aws_sdk_evs.types.instance_type_esx_versions_list.deserialize_aws_json_1_0(
                data["instanceTypeEsxVersions"]
            )
        )
    else:
        raise DeserializationError(
            "GetVersionsResponse.instance_type_esx_versions required"
        )
    return out
