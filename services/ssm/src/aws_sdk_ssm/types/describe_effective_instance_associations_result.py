"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeEffectiveInstanceAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_association_list
    import aws_sdk_ssm.types.next_token


class DescribeEffectiveInstanceAssociationsResult(TypedDict, closed=True):
    associations: NotRequired[
        "aws_sdk_ssm.types.instance_association_list.InstanceAssociationList"
    ]
    """<p>The associations for the requested managed node.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEffectiveInstanceAssociationsResult) -> dict:
    out: dict = {}
    if "associations" in value:
        import aws_sdk_ssm.types.instance_association_list

        out["Associations"] = (
            aws_sdk_ssm.types.instance_association_list.serialize_aws_json_1_1(
                value["associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEffectiveInstanceAssociationsResult:
    out: DescribeEffectiveInstanceAssociationsResult = {}  # type: ignore[typeddict-item]
    if "Associations" in data:
        import aws_sdk_ssm.types.instance_association_list

        out["associations"] = (
            aws_sdk_ssm.types.instance_association_list.deserialize_aws_json_1_1(
                data["Associations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
