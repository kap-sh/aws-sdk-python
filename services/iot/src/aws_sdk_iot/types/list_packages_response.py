"""Generated from Smithy shape ``com.amazonaws.iot#ListPackagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.package_summary_list


class ListPackagesResponse(TypedDict, closed=True):
    package_summaries: NotRequired[
        "aws_sdk_iot.types.package_summary_list.PackageSummaryList"
    ]
    """<p>The software package summary.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackagesResponse) -> dict:
    out: dict = {}
    if "package_summaries" in value:
        import aws_sdk_iot.types.package_summary_list

        out["packageSummaries"] = aws_sdk_iot.types.package_summary_list.serialize_json(
            value["package_summaries"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPackagesResponse:
    out: ListPackagesResponse = {}  # type: ignore[typeddict-item]
    if "packageSummaries" in data:
        import aws_sdk_iot.types.package_summary_list

        out["package_summaries"] = (
            aws_sdk_iot.types.package_summary_list.deserialize_json(
                data["packageSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
