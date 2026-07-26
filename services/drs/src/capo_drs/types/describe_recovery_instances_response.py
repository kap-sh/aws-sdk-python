"""Generated from Smithy shape ``com.amazonaws.drs#DescribeRecoveryInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.describe_recovery_instances_items
    import capo_drs.types.pagination_token


class DescribeRecoveryInstancesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Recovery Instance to retrieve.</p>"""
    items: NotRequired[
        "capo_drs.types.describe_recovery_instances_items.DescribeRecoveryInstancesItems"
    ]
    """<p>An array of Recovery Instances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecoveryInstancesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "items" in value:
        import capo_drs.types.describe_recovery_instances_items

        out["items"] = capo_drs.types.describe_recovery_instances_items.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> DescribeRecoveryInstancesResponse:
    out: DescribeRecoveryInstancesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "items" in data:
        import capo_drs.types.describe_recovery_instances_items

        out["items"] = (
            capo_drs.types.describe_recovery_instances_items.deserialize_json(
                data["items"]
            )
        )
    return out
