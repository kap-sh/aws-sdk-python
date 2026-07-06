"""Generated from Smithy shape ``com.amazonaws.rds#OptionGroupMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class OptionGroupMembership(TypedDict, closed=True):
    option_group_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the option group that the instance belongs to.</p>"""
    status: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The status of the DB instance's option group membership. Valid values are: <code>in-sync</code>, <code>pending-apply</code>, <code>pending-removal</code>, <code>pending-maintenance-apply</code>, <code>pending-maintenance-removal</code>, <code>applying</code>, <code>removing</code>, and <code>failed</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionGroupMembership, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "option_group_name" in value:
        pairs.append((f"{prefix}.OptionGroupName", str(value["option_group_name"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_query(el: Element) -> OptionGroupMembership:
    out: OptionGroupMembership = {}  # type: ignore[typeddict-item]
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
