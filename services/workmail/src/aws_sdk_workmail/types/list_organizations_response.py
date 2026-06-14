"""Generated from Smithy shape ``com.amazonaws.workmail#ListOrganizationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.next_token
    import aws_sdk_workmail.types.organization_summaries


class ListOrganizationsResponse(TypedDict):
    organization_summaries: NotRequired[
        "aws_sdk_workmail.types.organization_summaries.OrganizationSummaries"
    ]
    """<p>The overview of owned organizations presented as a list of organization summaries.</p>"""
    next_token: NotRequired["aws_sdk_workmail.types.next_token.NextToken"]
    r"""<p>The token to use to retrieve the next page of results. The value is \"null\" when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOrganizationsResponse) -> dict:
    out: dict = {}
    if "organization_summaries" in value:
        import aws_sdk_workmail.types.organization_summaries

        out["OrganizationSummaries"] = (
            aws_sdk_workmail.types.organization_summaries.serialize_aws_json_1_1(
                value["organization_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOrganizationsResponse:
    out: ListOrganizationsResponse = {}  # type: ignore[typeddict-item]
    if "OrganizationSummaries" in data:
        import aws_sdk_workmail.types.organization_summaries

        out["organization_summaries"] = (
            aws_sdk_workmail.types.organization_summaries.deserialize_aws_json_1_1(
                data["OrganizationSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
