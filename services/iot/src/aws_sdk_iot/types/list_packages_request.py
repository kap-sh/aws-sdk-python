"""Generated from Smithy shape ``com.amazonaws.iot#ListPackagesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.package_catalog_max_results


class ListPackagesRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_iot.types.package_catalog_max_results.PackageCatalogMaxResults"
    ]
    """<p>The maximum number of results returned at one time.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPackagesRequest:
    out: ListPackagesRequest = {}  # type: ignore[typeddict-item]
    return out
