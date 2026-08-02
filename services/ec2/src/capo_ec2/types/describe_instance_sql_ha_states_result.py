"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceSqlHaStatesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.next_token
    import capo_ec2.types.registered_instance_list


class DescribeInstanceSqlHaStatesResult(TypedDict, closed=True):
    instances: NotRequired[
        "capo_ec2.types.registered_instance_list.RegisteredInstanceList"
    ]
    """<p>Information about the SQL Server High Availability instances.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceSqlHaStatesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instances" in value:
        import capo_ec2.types.registered_instance_list

        capo_ec2.types.registered_instance_list.serialize_ec2_query(
            value["instances"], pairs, f"{key_prefix}InstanceSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInstanceSqlHaStatesResult:
    out: DescribeInstanceSqlHaStatesResult = {}  # type: ignore[typeddict-item]
    if el.find("InstanceSet") is not None:
        import capo_ec2.types.registered_instance_list

        out["instances"] = (
            capo_ec2.types.registered_instance_list.deserialize_ec2_query(
                el, "InstanceSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
