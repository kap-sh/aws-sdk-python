"""Generated from Smithy shape ``com.amazonaws.memorydb#ACLsUpdateStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.acl_name


class ACLsUpdateStatus(TypedDict, closed=True):
    acl_to_apply: NotRequired["aws_sdk_memorydb.types.acl_name.ACLName"]
    """<p>A list of ACLs pending to be applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ACLsUpdateStatus) -> dict:
    out: dict = {}
    if "acl_to_apply" in value:
        out["ACLToApply"] = value["acl_to_apply"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ACLsUpdateStatus:
    out: ACLsUpdateStatus = {}  # type: ignore[typeddict-item]
    if "ACLToApply" in data:
        out["acl_to_apply"] = data["ACLToApply"]
    return out
