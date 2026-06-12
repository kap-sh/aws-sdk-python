"""Generated from Smithy shape ``com.amazonaws.codecommit#SymbolicLinkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.symbolic_link

SymbolicLinkList: TypeAlias = list[
    "aws_sdk_codecommit.types.symbolic_link.SymbolicLink"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SymbolicLinkList) -> list:
    import aws_sdk_codecommit.types.symbolic_link

    out: list = []
    for item in value:
        out.append(aws_sdk_codecommit.types.symbolic_link.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SymbolicLinkList:
    import aws_sdk_codecommit.types.symbolic_link

    out: SymbolicLinkList = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.symbolic_link.deserialize_aws_json_1_1(item)
        )
    return out
