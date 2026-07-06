"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.association_edge_type
    import aws_sdk_sagemaker.types.association_entity_arn
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_associations_by
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.timestamp


class ListAssociationsRequest(TypedDict, closed=True):
    source_arn: NotRequired[
        "aws_sdk_sagemaker.types.association_entity_arn.AssociationEntityArn"
    ]
    """<p>A filter that returns only associations with the specified source ARN.</p>"""
    destination_arn: NotRequired[
        "aws_sdk_sagemaker.types.association_entity_arn.AssociationEntityArn"
    ]
    """<p>A filter that returns only associations with the specified destination Amazon Resource Name (ARN).</p>"""
    source_type: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>A filter that returns only associations with the specified source type.</p>"""
    destination_type: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>A filter that returns only associations with the specified destination type.</p>"""
    association_type: NotRequired[
        "aws_sdk_sagemaker.types.association_edge_type.AssociationEdgeType"
    ]
    """<p>A filter that returns only associations of the specified type.</p>"""
    created_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only associations created on or after the specified time.</p>"""
    created_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only associations created on or before the specified time.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.sort_associations_by.SortAssociationsBy"
    ]
    """<p>The property used to sort results. The default value is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order. The default value is <code>Descending</code>.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous call to <code>ListAssociations</code> didn't return the full set of associations, the call returns a token for getting the next set of associations.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of associations to return in the response. The default value is 10.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssociationsRequest) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "destination_type" in value:
        out["DestinationType"] = value["destination_type"]
    if "association_type" in value:
        import aws_sdk_sagemaker.types.association_edge_type

        out["AssociationType"] = (
            aws_sdk_sagemaker.types.association_edge_type.serialize_aws_json_1_1(
                value["association_type"]
            )
        )
    if "created_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedAfter"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedBefore"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.sort_associations_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.sort_associations_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssociationsRequest:
    out: ListAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "DestinationArn" in data:
        out["destination_arn"] = data["DestinationArn"]
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    if "DestinationType" in data:
        out["destination_type"] = data["DestinationType"]
    if "AssociationType" in data:
        import aws_sdk_sagemaker.types.association_edge_type

        out["association_type"] = (
            aws_sdk_sagemaker.types.association_edge_type.deserialize_aws_json_1_1(
                data["AssociationType"]
            )
        )
    if "CreatedAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedAfter"]
            )
        )
    if "CreatedBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedBefore"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.sort_associations_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.sort_associations_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
