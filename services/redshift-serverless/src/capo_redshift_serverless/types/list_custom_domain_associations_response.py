"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListCustomDomainAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.association_list
    import capo_redshift_serverless.types.pagination_token


class ListCustomDomainAssociationsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""
    associations: NotRequired[
        "capo_redshift_serverless.types.association_list.AssociationList"
    ]
    """<p>A list of Association objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCustomDomainAssociationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "associations" in value:
        import capo_redshift_serverless.types.association_list

        out["associations"] = (
            capo_redshift_serverless.types.association_list.serialize_aws_json_1_1(
                value["associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCustomDomainAssociationsResponse:
    out: ListCustomDomainAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "associations" in data:
        import capo_redshift_serverless.types.association_list

        out["associations"] = (
            capo_redshift_serverless.types.association_list.deserialize_aws_json_1_1(
                data["associations"]
            )
        )
    return out
