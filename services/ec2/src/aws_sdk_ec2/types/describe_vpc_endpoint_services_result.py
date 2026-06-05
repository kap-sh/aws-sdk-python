"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointServicesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_detail_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class DescribeVpcEndpointServicesResult(TypedDict):
    service_names: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The supported services.</p>"""
    service_details: NotRequired[
        "aws_sdk_ec2.types.service_detail_set.ServiceDetailSet"
    ]
    """<p>Information about the service.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEndpointServicesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "service_names" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["service_names"], pairs, f"{prefix}.ServiceNameSet"
        )
    if "service_details" in value:
        import aws_sdk_ec2.types.service_detail_set

        aws_sdk_ec2.types.service_detail_set.serialize_ec2_query(
            value["service_details"], pairs, f"{prefix}.ServiceDetailSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcEndpointServicesResult:
    out: DescribeVpcEndpointServicesResult = {}  # type: ignore[typeddict-item]
    if el.find("ServiceNameSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["service_names"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "ServiceNameSet"
            )
        )
    if el.find("ServiceDetailSet") is not None:
        import aws_sdk_ec2.types.service_detail_set

        out["service_details"] = (
            aws_sdk_ec2.types.service_detail_set.deserialize_ec2_query(
                el, "ServiceDetailSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
