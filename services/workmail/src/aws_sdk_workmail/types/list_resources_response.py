"""Generated from Smithy shape ``com.amazonaws.workmail#ListResourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.next_token
    import aws_sdk_workmail.types.resources


class ListResourcesResponse(TypedDict):
    resources: NotRequired["aws_sdk_workmail.types.resources.Resources"]
    """<p>One page of the organization's resource representation.</p>"""
    next_token: NotRequired["aws_sdk_workmail.types.next_token.NextToken"]
    """<p> The token used to paginate through all the organization's resources. While results are still available, it has an associated value. When the last page is reached, the token is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcesResponse) -> dict:
    out: dict = {}
    if "resources" in value:
        import aws_sdk_workmail.types.resources

        out["Resources"] = aws_sdk_workmail.types.resources.serialize_aws_json_1_1(
            value["resources"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcesResponse:
    out: ListResourcesResponse = {}  # type: ignore[typeddict-item]
    if "Resources" in data:
        import aws_sdk_workmail.types.resources

        out["resources"] = aws_sdk_workmail.types.resources.deserialize_aws_json_1_1(
            data["Resources"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
