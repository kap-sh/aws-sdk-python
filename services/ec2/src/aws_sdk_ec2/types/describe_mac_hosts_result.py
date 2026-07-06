"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMacHostsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.mac_host_list
    import aws_sdk_ec2.types.string


class DescribeMacHostsResult(TypedDict, closed=True):
    mac_hosts: NotRequired["aws_sdk_ec2.types.mac_host_list.MacHostList"]
    """<p> Information about the EC2 Mac Dedicated Hosts. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeMacHostsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "mac_hosts" in value:
        import aws_sdk_ec2.types.mac_host_list

        aws_sdk_ec2.types.mac_host_list.serialize_ec2_query(
            value["mac_hosts"], pairs, f"{prefix}.MacHostSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeMacHostsResult:
    out: DescribeMacHostsResult = {}  # type: ignore[typeddict-item]
    if el.find("MacHostSet") is not None:
        import aws_sdk_ec2.types.mac_host_list

        out["mac_hosts"] = aws_sdk_ec2.types.mac_host_list.deserialize_ec2_query(
            el, "MacHostSet"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
