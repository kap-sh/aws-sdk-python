"""Generated from Smithy shape ``com.amazonaws.ram#ListSourceAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.max_results
    import aws_sdk_ram.types.resource_share_arn_list
    import aws_sdk_ram.types.resource_share_association_status
    import aws_sdk_ram.types.string


class ListSourceAssociationsRequest(TypedDict):
    resource_share_arns: NotRequired[
        "aws_sdk_ram.types.resource_share_arn_list.ResourceShareArnList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the resource shares for which you want to retrieve source associations.</p>"""
    source_id: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The identifier of the source for which you want to retrieve associations. This can be an account ID, Amazon Resource Name (ARN), organization ID, or organization path.</p>"""
    source_type: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The type of source for which you want to retrieve associations.</p>"""
    association_status: NotRequired[
        "aws_sdk_ram.types.resource_share_association_status.ResourceShareAssociationStatus"
    ]
    """<p>The status of the source associations that you want to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""
    max_results: NotRequired["aws_sdk_ram.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceAssociationsRequest) -> dict:
    out: dict = {}
    if "resource_share_arns" in value:
        import aws_sdk_ram.types.resource_share_arn_list

        out["resourceShareArns"] = (
            aws_sdk_ram.types.resource_share_arn_list.serialize_json(
                value["resource_share_arns"]
            )
        )
    if "source_id" in value:
        out["sourceId"] = value["source_id"]
    if "source_type" in value:
        out["sourceType"] = value["source_type"]
    if "association_status" in value:
        import aws_sdk_ram.types.resource_share_association_status

        out["associationStatus"] = (
            aws_sdk_ram.types.resource_share_association_status.serialize_json(
                value["association_status"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListSourceAssociationsRequest:
    out: ListSourceAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "resourceShareArns" in data:
        import aws_sdk_ram.types.resource_share_arn_list

        out["resource_share_arns"] = (
            aws_sdk_ram.types.resource_share_arn_list.deserialize_json(
                data["resourceShareArns"]
            )
        )
    if "sourceId" in data:
        out["source_id"] = data["sourceId"]
    if "sourceType" in data:
        out["source_type"] = data["sourceType"]
    if "associationStatus" in data:
        import aws_sdk_ram.types.resource_share_association_status

        out["association_status"] = (
            aws_sdk_ram.types.resource_share_association_status.deserialize_json(
                data["associationStatus"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
