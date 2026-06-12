"""Generated from Smithy shape ``com.amazonaws.organizations#ListParentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.next_token
    import aws_sdk_organizations.types.parents


class ListParentsResponse(TypedDict):
    parents: NotRequired["aws_sdk_organizations.types.parents.Parents"]
    """<p>A list of parents for the specified child account or OU.</p>"""
    next_token: NotRequired["aws_sdk_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListParentsResponse) -> dict:
    out: dict = {}
    if "parents" in value:
        import aws_sdk_organizations.types.parents

        out["Parents"] = aws_sdk_organizations.types.parents.serialize_aws_json_1_1(
            value["parents"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListParentsResponse:
    out: ListParentsResponse = {}  # type: ignore[typeddict-item]
    if "Parents" in data:
        import aws_sdk_organizations.types.parents

        out["parents"] = aws_sdk_organizations.types.parents.deserialize_aws_json_1_1(
            data["Parents"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
