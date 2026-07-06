"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceSqlHaHistoryStatesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.registered_instance_list


class DescribeInstanceSqlHaHistoryStatesResult(TypedDict, closed=True):
    instances: NotRequired[
        "aws_sdk_ec2.types.registered_instance_list.RegisteredInstanceList"
    ]
    """<p>Information about the historical SQL Server High Availability states of the SQL Server High Availability instances.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceSqlHaHistoryStatesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instances" in value:
        import aws_sdk_ec2.types.registered_instance_list

        aws_sdk_ec2.types.registered_instance_list.serialize_ec2_query(
            value["instances"], pairs, f"{prefix}.InstanceSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInstanceSqlHaHistoryStatesResult:
    out: DescribeInstanceSqlHaHistoryStatesResult = {}  # type: ignore[typeddict-item]
    if el.find("InstanceSet") is not None:
        import aws_sdk_ec2.types.registered_instance_list

        out["instances"] = (
            aws_sdk_ec2.types.registered_instance_list.deserialize_ec2_query(
                el, "InstanceSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
