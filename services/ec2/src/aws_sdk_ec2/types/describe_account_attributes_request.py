"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAccountAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_attribute_name_string_list
    import aws_sdk_ec2.types.boolean


class DescribeAccountAttributesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    attribute_names: NotRequired[
        "aws_sdk_ec2.types.account_attribute_name_string_list.AccountAttributeNameStringList"
    ]
    """<p>The account attribute names.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAccountAttributesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "attribute_names" in value:
        import aws_sdk_ec2.types.account_attribute_name_string_list

        aws_sdk_ec2.types.account_attribute_name_string_list.serialize_ec2_query(
            value["attribute_names"], pairs, f"{prefix}.AttributeName"
        )


def deserialize_ec2_query(el: Element) -> DescribeAccountAttributesRequest:
    out: DescribeAccountAttributesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("AttributeName") is not None:
        import aws_sdk_ec2.types.account_attribute_name_string_list

        out["attribute_names"] = (
            aws_sdk_ec2.types.account_attribute_name_string_list.deserialize_ec2_query(
                el, "AttributeName"
            )
        )
    return out
