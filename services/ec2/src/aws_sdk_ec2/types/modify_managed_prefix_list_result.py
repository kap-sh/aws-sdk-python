"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyManagedPrefixListResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.managed_prefix_list


class ModifyManagedPrefixListResult(TypedDict):
    prefix_list: NotRequired["aws_sdk_ec2.types.managed_prefix_list.ManagedPrefixList"]
    """<p>Information about the prefix list.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyManagedPrefixListResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "prefix_list" in value:
        import aws_sdk_ec2.types.managed_prefix_list

        aws_sdk_ec2.types.managed_prefix_list.serialize_ec2_query(
            value["prefix_list"], pairs, f"{prefix}.PrefixList"
        )


def deserialize_ec2_query(el: Element) -> ModifyManagedPrefixListResult:
    out: ModifyManagedPrefixListResult = {}  # type: ignore[typeddict-item]
    child_prefix_list = el.find("PrefixList")
    if child_prefix_list is not None:
        import aws_sdk_ec2.types.managed_prefix_list

        out["prefix_list"] = (
            aws_sdk_ec2.types.managed_prefix_list.deserialize_ec2_query(
                child_prefix_list
            )
        )
    return out
