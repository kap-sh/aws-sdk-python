"""Generated from Smithy shape ``com.amazonaws.organizations#ListChildrenResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_organizations.types.children
    import aws_sdk_organizations.types.next_token


class ListChildrenResponse(TypedDict):
    children: NotRequired["aws_sdk_organizations.types.children.Children"]
    """<p>The list of children of the specified parent container.</p>"""
    next_token: NotRequired["aws_sdk_organizations.types.next_token.NextToken"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListChildrenResponse) -> dict:
    out: dict = {}
    if "children" in value:
        import aws_sdk_organizations.types.children

        out["Children"] = aws_sdk_organizations.types.children.serialize_aws_json_1_1(
            value["children"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListChildrenResponse:
    out: ListChildrenResponse = {}  # type: ignore[typeddict-item]
    if "Children" in data:
        import aws_sdk_organizations.types.children

        out["children"] = aws_sdk_organizations.types.children.deserialize_aws_json_1_1(
            data["Children"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
