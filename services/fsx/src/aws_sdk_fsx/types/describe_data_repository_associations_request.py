"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeDataRepositoryAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.data_repository_association_ids
    import aws_sdk_fsx.types.filters
    import aws_sdk_fsx.types.limited_max_results
    import aws_sdk_fsx.types.next_token


class DescribeDataRepositoryAssociationsRequest(TypedDict, closed=True):
    association_ids: NotRequired[
        "aws_sdk_fsx.types.data_repository_association_ids.DataRepositoryAssociationIds"
    ]
    """<p>IDs of the data repository associations whose descriptions you want to retrieve (String).</p>"""
    filters: NotRequired["aws_sdk_fsx.types.filters.Filters"]
    max_results: NotRequired["aws_sdk_fsx.types.limited_max_results.LimitedMaxResults"]
    """<p>The maximum number of resources to return in the response. This value must be an integer greater than zero.</p>"""
    next_token: NotRequired["aws_sdk_fsx.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDataRepositoryAssociationsRequest) -> dict:
    out: dict = {}
    if "association_ids" in value:
        import aws_sdk_fsx.types.data_repository_association_ids

        out["AssociationIds"] = (
            aws_sdk_fsx.types.data_repository_association_ids.serialize_aws_json_1_1(
                value["association_ids"]
            )
        )
    if "filters" in value:
        import aws_sdk_fsx.types.filters

        out["Filters"] = aws_sdk_fsx.types.filters.serialize_aws_json_1_1(
            value["filters"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDataRepositoryAssociationsRequest:
    out: DescribeDataRepositoryAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "AssociationIds" in data:
        import aws_sdk_fsx.types.data_repository_association_ids

        out["association_ids"] = (
            aws_sdk_fsx.types.data_repository_association_ids.deserialize_aws_json_1_1(
                data["AssociationIds"]
            )
        )
    if "Filters" in data:
        import aws_sdk_fsx.types.filters

        out["filters"] = aws_sdk_fsx.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
