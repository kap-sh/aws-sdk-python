"""Generated from Smithy shape ``com.amazonaws.iot#ListPackageVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.package_catalog_max_results
    import aws_sdk_iot.types.package_name
    import aws_sdk_iot.types.package_version_status


class ListPackageVersionsRequest(TypedDict):
    package_name: "aws_sdk_iot.types.package_name.PackageName"
    """<p>The name of the target software package.</p>"""
    status: NotRequired["aws_sdk_iot.types.package_version_status.PackageVersionStatus"]
    """<p>The status of the package version. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle\">Package version lifecycle</a>.</p>"""
    max_results: NotRequired[
        "aws_sdk_iot.types.package_catalog_max_results.PackageCatalogMaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackageVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPackageVersionsRequest:
    out: ListPackageVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
