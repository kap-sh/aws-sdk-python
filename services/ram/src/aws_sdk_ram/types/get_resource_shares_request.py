"""Generated from Smithy shape ``com.amazonaws.ram#GetResourceSharesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ram.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ram.types.integer
    import aws_sdk_ram.types.max_results
    import aws_sdk_ram.types.resource_owner
    import aws_sdk_ram.types.resource_share_arn_list
    import aws_sdk_ram.types.resource_share_status
    import aws_sdk_ram.types.string
    import aws_sdk_ram.types.tag_filters


class GetResourceSharesRequest(TypedDict):
    resource_share_arns: NotRequired[
        "aws_sdk_ram.types.resource_share_arn_list.ResourceShareArnList"
    ]
    r"""<p>Specifies the <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> of individual resource shares that you want information about.</p>"""
    resource_share_status: NotRequired[
        "aws_sdk_ram.types.resource_share_status.ResourceShareStatus"
    ]
    """<p>Specifies that you want to retrieve details of only those resource shares that have this status.</p>"""
    resource_owner: "aws_sdk_ram.types.resource_owner.ResourceOwner"
    """<p>Specifies that you want to retrieve details of only those resource shares that match the following:</p> <ul> <li> <p> <b> <code>SELF</code> </b> – resource shares that your account shares with other accounts</p> </li> <li> <p> <b> <code>OTHER-ACCOUNTS</code> </b> – resource shares that other accounts share with your account</p> </li> </ul>"""
    name: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>Specifies the name of an individual resource share that you want to retrieve details about.</p>"""
    tag_filters: NotRequired["aws_sdk_ram.types.tag_filters.TagFilters"]
    """<p>Specifies that you want to retrieve details of only those resource shares that match the specified tag keys and values.</p>"""
    next_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_ram.types.max_results.MaxResults"]
    """<p>Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""
    permission_arn: NotRequired["aws_sdk_ram.types.string.String"]
    r"""<p>Specifies that you want to retrieve details of only those resource shares that use the managed permission with this <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Name (ARN)</a>.</p>"""
    permission_version: NotRequired["aws_sdk_ram.types.integer.Integer"]
    """<p>Specifies that you want to retrieve details for only those resource shares that use the specified version of the managed permission.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceSharesRequest) -> dict:
    out: dict = {}
    if "resource_share_arns" in value:
        import aws_sdk_ram.types.resource_share_arn_list

        out["resourceShareArns"] = (
            aws_sdk_ram.types.resource_share_arn_list.serialize_json(
                value["resource_share_arns"]
            )
        )
    if "resource_share_status" in value:
        import aws_sdk_ram.types.resource_share_status

        out["resourceShareStatus"] = (
            aws_sdk_ram.types.resource_share_status.serialize_json(
                value["resource_share_status"]
            )
        )
    import aws_sdk_ram.types.resource_owner

    out["resourceOwner"] = aws_sdk_ram.types.resource_owner.serialize_json(
        value["resource_owner"]
    )
    if "name" in value:
        out["name"] = value["name"]
    if "tag_filters" in value:
        import aws_sdk_ram.types.tag_filters

        out["tagFilters"] = aws_sdk_ram.types.tag_filters.serialize_json(
            value["tag_filters"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "permission_arn" in value:
        out["permissionArn"] = value["permission_arn"]
    if "permission_version" in value:
        out["permissionVersion"] = value["permission_version"]
    return out


def deserialize_json(data: dict) -> GetResourceSharesRequest:
    out: GetResourceSharesRequest = {}  # type: ignore[typeddict-item]
    if "resourceShareArns" in data:
        import aws_sdk_ram.types.resource_share_arn_list

        out["resource_share_arns"] = (
            aws_sdk_ram.types.resource_share_arn_list.deserialize_json(
                data["resourceShareArns"]
            )
        )
    if "resourceShareStatus" in data:
        import aws_sdk_ram.types.resource_share_status

        out["resource_share_status"] = (
            aws_sdk_ram.types.resource_share_status.deserialize_json(
                data["resourceShareStatus"]
            )
        )
    if "resourceOwner" in data:
        import aws_sdk_ram.types.resource_owner

        out["resource_owner"] = aws_sdk_ram.types.resource_owner.deserialize_json(
            data["resourceOwner"]
        )
    else:
        raise DeserializationError("GetResourceSharesRequest.resource_owner required")
    if "name" in data:
        out["name"] = data["name"]
    if "tagFilters" in data:
        import aws_sdk_ram.types.tag_filters

        out["tag_filters"] = aws_sdk_ram.types.tag_filters.deserialize_json(
            data["tagFilters"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "permissionArn" in data:
        out["permission_arn"] = data["permissionArn"]
    if "permissionVersion" in data:
        out["permission_version"] = data["permissionVersion"]
    return out
