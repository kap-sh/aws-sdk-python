"""Generated from Smithy shape ``com.amazonaws.fms#Routes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.route

Routes: TypeAlias = list["aws_sdk_fms.types.route.Route"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Routes) -> list:
    import aws_sdk_fms.types.route

    out: list = []
    for item in value:
        out.append(aws_sdk_fms.types.route.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Routes:
    import aws_sdk_fms.types.route

    out: Routes = []
    for item in data:
        out.append(aws_sdk_fms.types.route.deserialize_aws_json_1_1(item))
    return out
