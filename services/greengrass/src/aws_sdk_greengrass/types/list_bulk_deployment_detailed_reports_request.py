"""Generated from Smithy shape ``com.amazonaws.greengrass#ListBulkDeploymentDetailedReportsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class ListBulkDeploymentDetailedReportsRequest(TypedDict):
    bulk_deployment_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the bulk deployment."""
    max_results: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The maximum number of results to be returned per request."""
    next_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListBulkDeploymentDetailedReportsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBulkDeploymentDetailedReportsRequest:
    out: ListBulkDeploymentDetailedReportsRequest = {}  # type: ignore[typeddict-item]
    return out
