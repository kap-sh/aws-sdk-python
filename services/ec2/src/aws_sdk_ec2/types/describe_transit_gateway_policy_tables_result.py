"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayPolicyTablesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_policy_table_list


class DescribeTransitGatewayPolicyTablesResult(TypedDict):
    transit_gateway_policy_tables: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table_list.TransitGatewayPolicyTableList"
    ]
    """<p>Describes the transit gateway policy tables.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTransitGatewayPolicyTablesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_policy_tables" in value:
        import aws_sdk_ec2.types.transit_gateway_policy_table_list

        aws_sdk_ec2.types.transit_gateway_policy_table_list.serialize_ec2_query(
            value["transit_gateway_policy_tables"],
            pairs,
            f"{prefix}.TransitGatewayPolicyTables",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTransitGatewayPolicyTablesResult:
    out: DescribeTransitGatewayPolicyTablesResult = {}  # type: ignore[typeddict-item]
    if el.find("TransitGatewayPolicyTables") is not None:
        import aws_sdk_ec2.types.transit_gateway_policy_table_list

        out["transit_gateway_policy_tables"] = (
            aws_sdk_ec2.types.transit_gateway_policy_table_list.deserialize_ec2_query(
                el, "TransitGatewayPolicyTables"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
