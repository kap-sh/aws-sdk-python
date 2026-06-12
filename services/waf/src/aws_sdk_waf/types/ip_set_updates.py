"""Generated from Smithy shape ``com.amazonaws.waf#IPSetUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf.types.ip_set_update

IPSetUpdates: TypeAlias = list["aws_sdk_waf.types.ip_set_update.IPSetUpdate"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPSetUpdates) -> list:
    import aws_sdk_waf.types.ip_set_update

    out: list = []
    for item in value:
        out.append(aws_sdk_waf.types.ip_set_update.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IPSetUpdates:
    import aws_sdk_waf.types.ip_set_update

    out: IPSetUpdates = []
    for item in data:
        out.append(aws_sdk_waf.types.ip_set_update.deserialize_aws_json_1_1(item))
    return out
