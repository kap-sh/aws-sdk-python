"""Generated from Smithy shape ``com.amazonaws.waf#WebACLUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf.types.web_acl_update

WebACLUpdates: TypeAlias = list["capo_waf.types.web_acl_update.WebACLUpdate"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebACLUpdates) -> list:
    import capo_waf.types.web_acl_update

    out: list = []
    for item in value:
        out.append(capo_waf.types.web_acl_update.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WebACLUpdates:
    import capo_waf.types.web_acl_update

    out: WebACLUpdates = []
    for item in data:
        out.append(capo_waf.types.web_acl_update.deserialize_aws_json_1_1(item))
    return out
