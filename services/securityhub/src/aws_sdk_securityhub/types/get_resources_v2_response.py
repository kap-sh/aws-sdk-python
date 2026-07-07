"""Generated from Smithy shape ``com.amazonaws.securityhub#GetResourcesV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.resources


class GetResourcesV2Response(TypedDict, closed=True):
    resources: NotRequired["aws_sdk_securityhub.types.resources.Resources"]
    """<p>An array of resources returned by the operation.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results. Otherwise, this parameter is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcesV2Response) -> dict:
    out: dict = {}
    if "resources" in value:
        import aws_sdk_securityhub.types.resources

        out["Resources"] = aws_sdk_securityhub.types.resources.serialize_json(
            value["resources"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetResourcesV2Response:
    out: GetResourcesV2Response = {}  # type: ignore[typeddict-item]
    if "Resources" in data:
        import aws_sdk_securityhub.types.resources

        out["resources"] = aws_sdk_securityhub.types.resources.deserialize_json(
            data["Resources"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
