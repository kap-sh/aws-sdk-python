"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInstanceAssociationsStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.instance_association_status_infos
    import capo_ssm.types.next_token


class DescribeInstanceAssociationsStatusResult(TypedDict, closed=True):
    instance_association_status_infos: NotRequired[
        "capo_ssm.types.instance_association_status_infos.InstanceAssociationStatusInfos"
    ]
    """<p>Status information about the association.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstanceAssociationsStatusResult) -> dict:
    out: dict = {}
    if "instance_association_status_infos" in value:
        import capo_ssm.types.instance_association_status_infos

        out["InstanceAssociationStatusInfos"] = (
            capo_ssm.types.instance_association_status_infos.serialize_aws_json_1_1(
                value["instance_association_status_infos"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstanceAssociationsStatusResult:
    out: DescribeInstanceAssociationsStatusResult = {}  # type: ignore[typeddict-item]
    if data.get("InstanceAssociationStatusInfos") is not None:
        import capo_ssm.types.instance_association_status_infos

        out["instance_association_status_infos"] = (
            capo_ssm.types.instance_association_status_infos.deserialize_aws_json_1_1(
                data["InstanceAssociationStatusInfos"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
