"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCoverageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.covered_resources
    import aws_sdk_inspector2.types.next_token


class ListCoverageResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""
    covered_resources: NotRequired[
        "aws_sdk_inspector2.types.covered_resources.CoveredResources"
    ]
    """<p>An object that contains details on the covered resources in your environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoverageResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "covered_resources" in value:
        import aws_sdk_inspector2.types.covered_resources

        out["coveredResources"] = (
            aws_sdk_inspector2.types.covered_resources.serialize_json(
                value["covered_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCoverageResponse:
    out: ListCoverageResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "coveredResources" in data:
        import aws_sdk_inspector2.types.covered_resources

        out["covered_resources"] = (
            aws_sdk_inspector2.types.covered_resources.deserialize_json(
                data["coveredResources"]
            )
        )
    return out
