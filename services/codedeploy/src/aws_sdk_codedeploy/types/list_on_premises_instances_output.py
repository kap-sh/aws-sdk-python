"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListOnPremisesInstancesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.instance_name_list
    import aws_sdk_codedeploy.types.next_token


class ListOnPremisesInstancesOutput(TypedDict, closed=True):
    instance_names: NotRequired[
        "aws_sdk_codedeploy.types.instance_name_list.InstanceNameList"
    ]
    """<p>The list of matching on-premises instance names.</p>"""
    next_token: NotRequired["aws_sdk_codedeploy.types.next_token.NextToken"]
    """<p>If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list on-premises instances call to return the next set of on-premises instances in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOnPremisesInstancesOutput) -> dict:
    out: dict = {}
    if "instance_names" in value:
        import aws_sdk_codedeploy.types.instance_name_list

        out["instanceNames"] = (
            aws_sdk_codedeploy.types.instance_name_list.serialize_aws_json_1_1(
                value["instance_names"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOnPremisesInstancesOutput:
    out: ListOnPremisesInstancesOutput = {}  # type: ignore[typeddict-item]
    if "instanceNames" in data:
        import aws_sdk_codedeploy.types.instance_name_list

        out["instance_names"] = (
            aws_sdk_codedeploy.types.instance_name_list.deserialize_aws_json_1_1(
                data["instanceNames"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
