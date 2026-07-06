"""Generated from Smithy shape ``com.amazonaws.guardduty#ListCoverageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.coverage_resources
    import aws_sdk_guardduty.types.string


class ListCoverageResponse(TypedDict, closed=True):
    resources: NotRequired[
        "aws_sdk_guardduty.types.coverage_resources.CoverageResources"
    ]
    """<p>A list of resources and their attributes providing cluster details.</p>"""
    next_token: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoverageResponse) -> dict:
    out: dict = {}
    if "resources" in value:
        import aws_sdk_guardduty.types.coverage_resources

        out["resources"] = aws_sdk_guardduty.types.coverage_resources.serialize_json(
            value["resources"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCoverageResponse:
    out: ListCoverageResponse = {}  # type: ignore[typeddict-item]
    if "resources" in data:
        import aws_sdk_guardduty.types.coverage_resources

        out["resources"] = aws_sdk_guardduty.types.coverage_resources.deserialize_json(
            data["resources"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
