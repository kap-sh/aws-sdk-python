"""Generated from Smithy shape ``com.amazonaws.lightsail#AddOnRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.add_on_request

AddOnRequestList: TypeAlias = list["capo_lightsail.types.add_on_request.AddOnRequest"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddOnRequestList) -> list:
    import capo_lightsail.types.add_on_request

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.add_on_request.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AddOnRequestList:
    import capo_lightsail.types.add_on_request

    out: AddOnRequestList = []
    for item in data:
        out.append(capo_lightsail.types.add_on_request.deserialize_aws_json_1_1(item))
    return out
