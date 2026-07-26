"""Generated from Smithy shape ``com.amazonaws.outposts#AWSServiceNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.aws_service_name

AWSServiceNameList: TypeAlias = list[
    "capo_outposts.types.aws_service_name.AWSServiceName"
]


# --- restJson1 ser/de ---
def serialize_json(value: AWSServiceNameList) -> list:
    import capo_outposts.types.aws_service_name

    out: list = []
    for item in value:
        out.append(capo_outposts.types.aws_service_name.serialize_json(item))
    return out


def deserialize_json(data: list) -> AWSServiceNameList:
    import capo_outposts.types.aws_service_name

    out: AWSServiceNameList = []
    for item in data:
        out.append(capo_outposts.types.aws_service_name.deserialize_json(item))
    return out
