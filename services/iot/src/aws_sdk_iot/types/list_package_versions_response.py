"""Generated from Smithy shape ``com.amazonaws.iot#ListPackageVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.package_version_summary_list


class ListPackageVersionsResponse(TypedDict, closed=True):
    package_version_summaries: NotRequired[
        "aws_sdk_iot.types.package_version_summary_list.PackageVersionSummaryList"
    ]
    """<p>Lists the package versions associated to the package.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackageVersionsResponse) -> dict:
    out: dict = {}
    if "package_version_summaries" in value:
        import aws_sdk_iot.types.package_version_summary_list

        out["packageVersionSummaries"] = (
            aws_sdk_iot.types.package_version_summary_list.serialize_json(
                value["package_version_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPackageVersionsResponse:
    out: ListPackageVersionsResponse = {}  # type: ignore[typeddict-item]
    if "packageVersionSummaries" in data:
        import aws_sdk_iot.types.package_version_summary_list

        out["package_version_summaries"] = (
            aws_sdk_iot.types.package_version_summary_list.deserialize_json(
                data["packageVersionSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
