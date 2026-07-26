"""Generated from Smithy shape ``com.amazonaws.mediastore#AllowedMethods``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediastore.types.method_name

AllowedMethods: TypeAlias = list["capo_mediastore.types.method_name.MethodName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedMethods) -> list:
    import capo_mediastore.types.method_name

    out: list = []
    for item in value:
        out.append(capo_mediastore.types.method_name.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AllowedMethods:
    import capo_mediastore.types.method_name

    out: AllowedMethods = []
    for item in data:
        out.append(capo_mediastore.types.method_name.deserialize_aws_json_1_1(item))
    return out
