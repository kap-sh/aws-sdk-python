"""Generated from Smithy shape ``com.amazonaws.organizations#ListRootsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.next_token
    import aws_sdk_organizations.types.roots


class ListRootsResponse(TypedDict, closed=True):
    roots: NotRequired["aws_sdk_organizations.types.roots.Roots"]
    """<p>A list of roots that are defined in an organization.</p>"""
    next_token: NotRequired["aws_sdk_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRootsResponse) -> dict:
    out: dict = {}
    if "roots" in value:
        import aws_sdk_organizations.types.roots

        out["Roots"] = aws_sdk_organizations.types.roots.serialize_aws_json_1_1(
            value["roots"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRootsResponse:
    out: ListRootsResponse = {}  # type: ignore[typeddict-item]
    if "Roots" in data:
        import aws_sdk_organizations.types.roots

        out["roots"] = aws_sdk_organizations.types.roots.deserialize_aws_json_1_1(
            data["Roots"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
