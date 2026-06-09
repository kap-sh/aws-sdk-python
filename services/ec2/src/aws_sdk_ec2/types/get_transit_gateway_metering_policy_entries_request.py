"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayMeteringPolicyEntriesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_max_results
    import aws_sdk_ec2.types.transit_gateway_metering_policy_id


class GetTransitGatewayMeteringPolicyEntriesRequest(TypedDict):
    transit_gateway_metering_policy_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy_id.TransitGatewayMeteringPolicyId"
    ]
    """<p>The ID of the transit gateway metering policy to retrieve entries for.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters to apply when retrieving metering policy entries.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_max_results.TransitGatewayMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetTransitGatewayMeteringPolicyEntriesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_metering_policy_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayMeteringPolicyId",
                str(value["transit_gateway_metering_policy_id"]),
            )
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> GetTransitGatewayMeteringPolicyEntriesRequest:
    out: GetTransitGatewayMeteringPolicyEntriesRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_metering_policy_id = el.find("TransitGatewayMeteringPolicyId")
    if child_transit_gateway_metering_policy_id is not None:
        out["transit_gateway_metering_policy_id"] = str(
            child_transit_gateway_metering_policy_id.text or ""
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
