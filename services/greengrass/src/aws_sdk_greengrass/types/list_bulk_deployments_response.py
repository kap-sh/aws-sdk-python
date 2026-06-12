"""Generated from Smithy shape ``com.amazonaws.greengrass#ListBulkDeploymentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.bulk_deployments


class ListBulkDeploymentsResponse(TypedDict):
    bulk_deployments: NotRequired[
        "aws_sdk_greengrass.types.bulk_deployments.BulkDeployments"
    ]
    """A list of bulk deployments."""
    next_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListBulkDeploymentsResponse) -> dict:
    out: dict = {}
    if "bulk_deployments" in value:
        import aws_sdk_greengrass.types.bulk_deployments

        out["BulkDeployments"] = (
            aws_sdk_greengrass.types.bulk_deployments.serialize_json(
                value["bulk_deployments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBulkDeploymentsResponse:
    out: ListBulkDeploymentsResponse = {}  # type: ignore[typeddict-item]
    if "BulkDeployments" in data:
        import aws_sdk_greengrass.types.bulk_deployments

        out["bulk_deployments"] = (
            aws_sdk_greengrass.types.bulk_deployments.deserialize_json(
                data["BulkDeployments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
