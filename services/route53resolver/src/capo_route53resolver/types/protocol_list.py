"""Generated from Smithy shape ``com.amazonaws.route53resolver#ProtocolList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53resolver.types.protocol

ProtocolList: TypeAlias = list["capo_route53resolver.types.protocol.Protocol"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtocolList) -> list:
    import capo_route53resolver.types.protocol

    out: list = []
    for item in value:
        out.append(capo_route53resolver.types.protocol.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProtocolList:
    import capo_route53resolver.types.protocol

    out: ProtocolList = []
    for item in data:
        out.append(capo_route53resolver.types.protocol.deserialize_aws_json_1_1(item))
    return out
