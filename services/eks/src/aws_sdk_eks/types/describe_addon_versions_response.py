"""Generated from Smithy shape ``com.amazonaws.eks#DescribeAddonVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.addons
    import aws_sdk_eks.types.string


class DescribeAddonVersionsResponse(TypedDict, closed=True):
    addons: NotRequired["aws_sdk_eks.types.addons.Addons"]
    """<p>The list of available versions with Kubernetes version compatibility and other properties.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeAddonVersions</code> request. When the results of a <code>DescribeAddonVersions</code> request exceed <code>maxResults</code>, you can use this value to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAddonVersionsResponse) -> dict:
    out: dict = {}
    if "addons" in value:
        import aws_sdk_eks.types.addons

        out["addons"] = aws_sdk_eks.types.addons.serialize_json(value["addons"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeAddonVersionsResponse:
    out: DescribeAddonVersionsResponse = {}  # type: ignore[typeddict-item]
    if "addons" in data:
        import aws_sdk_eks.types.addons

        out["addons"] = aws_sdk_eks.types.addons.deserialize_json(data["addons"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
