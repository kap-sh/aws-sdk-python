"""Generated from Smithy shape ``com.amazonaws.ram#GetResourceShareInvitationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.max_results
    import aws_sdk_ram.types.resource_share_arn_list
    import aws_sdk_ram.types.resource_share_invitation_arn_list
    import aws_sdk_ram.types.string


class GetResourceShareInvitationsRequest(TypedDict):
    resource_share_invitation_arns: NotRequired[
        "aws_sdk_ram.types.resource_share_invitation_arn_list.ResourceShareInvitationArnList"
    ]
    r"""<p>Specifies the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> of the resource share invitations you want information about.</p>"""
    resource_share_arns: NotRequired[
        "aws_sdk_ram.types.resource_share_arn_list.ResourceShareArnList"
    ]
    r"""<p>Specifies that you want details about invitations only for the resource shares described by this list of <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> </p>"""
    next_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_ram.types.max_results.MaxResults"]
    """<p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceShareInvitationsRequest) -> dict:
    out: dict = {}
    if "resource_share_invitation_arns" in value:
        import aws_sdk_ram.types.resource_share_invitation_arn_list

        out["resourceShareInvitationArns"] = (
            aws_sdk_ram.types.resource_share_invitation_arn_list.serialize_json(
                value["resource_share_invitation_arns"]
            )
        )
    if "resource_share_arns" in value:
        import aws_sdk_ram.types.resource_share_arn_list

        out["resourceShareArns"] = (
            aws_sdk_ram.types.resource_share_arn_list.serialize_json(
                value["resource_share_arns"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> GetResourceShareInvitationsRequest:
    out: GetResourceShareInvitationsRequest = {}  # type: ignore[typeddict-item]
    if "resourceShareInvitationArns" in data:
        import aws_sdk_ram.types.resource_share_invitation_arn_list

        out["resource_share_invitation_arns"] = (
            aws_sdk_ram.types.resource_share_invitation_arn_list.deserialize_json(
                data["resourceShareInvitationArns"]
            )
        )
    if "resourceShareArns" in data:
        import aws_sdk_ram.types.resource_share_arn_list

        out["resource_share_arns"] = (
            aws_sdk_ram.types.resource_share_arn_list.deserialize_json(
                data["resourceShareArns"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
