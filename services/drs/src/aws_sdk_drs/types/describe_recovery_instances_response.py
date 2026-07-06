"""Generated from Smithy shape ``com.amazonaws.drs#DescribeRecoveryInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.describe_recovery_instances_items
    import aws_sdk_drs.types.pagination_token


class DescribeRecoveryInstancesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Recovery Instance to retrieve.</p>"""
    items: NotRequired[
        "aws_sdk_drs.types.describe_recovery_instances_items.DescribeRecoveryInstancesItems"
    ]
    """<p>An array of Recovery Instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecoveryInstancesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "items" in value:
        import aws_sdk_drs.types.describe_recovery_instances_items

        out["items"] = (
            aws_sdk_drs.types.describe_recovery_instances_items.serialize_json(
                value["items"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeRecoveryInstancesResponse:
    out: DescribeRecoveryInstancesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "items" in data:
        import aws_sdk_drs.types.describe_recovery_instances_items

        out["items"] = (
            aws_sdk_drs.types.describe_recovery_instances_items.deserialize_json(
                data["items"]
            )
        )
    return out
