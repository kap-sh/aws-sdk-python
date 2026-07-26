"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeUsersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.authentication_type
    import capo_appstream.types.integer
    import capo_appstream.types.string


class DescribeUsersRequest(TypedDict, closed=True):
    authentication_type: NotRequired[
        "capo_appstream.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type for the users in the user pool to describe. You must specify USERPOOL.</p>"""
    max_results: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The maximum size of each page of results.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeUsersRequest) -> dict:
    out: dict = {}
    if "authentication_type" in value:
        import capo_appstream.types.authentication_type

        out["AuthenticationType"] = (
            capo_appstream.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeUsersRequest:
    out: DescribeUsersRequest = {}  # type: ignore[typeddict-item]
    if "AuthenticationType" in data:
        import capo_appstream.types.authentication_type

        out["authentication_type"] = (
            capo_appstream.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
