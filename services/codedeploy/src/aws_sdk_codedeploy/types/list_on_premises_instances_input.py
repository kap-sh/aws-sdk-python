"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListOnPremisesInstancesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.next_token
    import aws_sdk_codedeploy.types.registration_status
    import aws_sdk_codedeploy.types.tag_filter_list


class ListOnPremisesInstancesInput(TypedDict):
    registration_status: NotRequired[
        "aws_sdk_codedeploy.types.registration_status.RegistrationStatus"
    ]
    """<p>The registration status of the on-premises instances:</p> <ul> <li> <p> <code>Deregistered</code>: Include deregistered on-premises instances in the resulting list.</p> </li> <li> <p> <code>Registered</code>: Include registered on-premises instances in the resulting list.</p> </li> </ul>"""
    tag_filters: NotRequired["aws_sdk_codedeploy.types.tag_filter_list.TagFilterList"]
    """<p>The on-premises instance tags that are used to restrict the on-premises instance names returned.</p>"""
    next_token: NotRequired["aws_sdk_codedeploy.types.next_token.NextToken"]
    """<p>An identifier returned from the previous list on-premises instances call. It can be used to return the next set of on-premises instances in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOnPremisesInstancesInput) -> dict:
    out: dict = {}
    if "registration_status" in value:
        import aws_sdk_codedeploy.types.registration_status

        out["registrationStatus"] = (
            aws_sdk_codedeploy.types.registration_status.serialize_aws_json_1_1(
                value["registration_status"]
            )
        )
    if "tag_filters" in value:
        import aws_sdk_codedeploy.types.tag_filter_list

        out["tagFilters"] = (
            aws_sdk_codedeploy.types.tag_filter_list.serialize_aws_json_1_1(
                value["tag_filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOnPremisesInstancesInput:
    out: ListOnPremisesInstancesInput = {}  # type: ignore[typeddict-item]
    if "registrationStatus" in data:
        import aws_sdk_codedeploy.types.registration_status

        out["registration_status"] = (
            aws_sdk_codedeploy.types.registration_status.deserialize_aws_json_1_1(
                data["registrationStatus"]
            )
        )
    if "tagFilters" in data:
        import aws_sdk_codedeploy.types.tag_filter_list

        out["tag_filters"] = (
            aws_sdk_codedeploy.types.tag_filter_list.deserialize_aws_json_1_1(
                data["tagFilters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
