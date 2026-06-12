"""Generated from Smithy shape ``com.amazonaws.waf#WebACLUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf.types.web_acl_update

WebACLUpdates: TypeAlias = list["aws_sdk_waf.types.web_acl_update.WebACLUpdate"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebACLUpdates) -> list:
    import aws_sdk_waf.types.web_acl_update

    out: list = []
    for item in value:
        out.append(aws_sdk_waf.types.web_acl_update.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WebACLUpdates:
    import aws_sdk_waf.types.web_acl_update

    out: WebACLUpdates = []
    for item in data:
        out.append(aws_sdk_waf.types.web_acl_update.deserialize_aws_json_1_1(item))
    return out
