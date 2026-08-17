"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeCapacityProvidersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.capacity_providers
    import capo_ecs.types.failures
    import capo_ecs.types.string


class DescribeCapacityProvidersResponse(TypedDict, closed=True):
    capacity_providers: NotRequired[
        "capo_ecs.types.capacity_providers.CapacityProviders"
    ]
    """<p>The list of capacity providers.</p>"""
    failures: NotRequired["capo_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeCapacityProviders</code> request. When the results of a <code>DescribeCapacityProviders</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCapacityProvidersResponse) -> dict:
    out: dict = {}
    if "capacity_providers" in value:
        import capo_ecs.types.capacity_providers

        out["capacityProviders"] = (
            capo_ecs.types.capacity_providers.serialize_aws_json_1_1(
                value["capacity_providers"]
            )
        )
    if "failures" in value:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCapacityProvidersResponse:
    out: DescribeCapacityProvidersResponse = {}  # type: ignore[typeddict-item]
    if data.get("capacityProviders") is not None:
        import capo_ecs.types.capacity_providers

        out["capacity_providers"] = (
            capo_ecs.types.capacity_providers.deserialize_aws_json_1_1(
                data["capacityProviders"]
            )
        )
    if data.get("failures") is not None:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
