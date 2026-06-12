"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanEc2InstanceWithFindingsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.ebs_volumes_result


class ScanEc2InstanceWithFindingsResult(TypedDict):
    ebs_volumes: NotRequired[
        "aws_sdk_guardduty.types.ebs_volumes_result.EbsVolumesResult"
    ]
    """<p>Describes the configuration of scanning EBS volumes as a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanEc2InstanceWithFindingsResult) -> dict:
    out: dict = {}
    if "ebs_volumes" in value:
        import aws_sdk_guardduty.types.ebs_volumes_result

        out["ebsVolumes"] = aws_sdk_guardduty.types.ebs_volumes_result.serialize_json(
            value["ebs_volumes"]
        )
    return out


def deserialize_json(data: dict) -> ScanEc2InstanceWithFindingsResult:
    out: ScanEc2InstanceWithFindingsResult = {}  # type: ignore[typeddict-item]
    if "ebsVolumes" in data:
        import aws_sdk_guardduty.types.ebs_volumes_result

        out["ebs_volumes"] = (
            aws_sdk_guardduty.types.ebs_volumes_result.deserialize_json(
                data["ebsVolumes"]
            )
        )
    return out
