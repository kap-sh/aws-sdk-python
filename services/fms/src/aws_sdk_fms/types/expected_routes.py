"""Generated from Smithy shape ``com.amazonaws.fms#ExpectedRoutes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.expected_route

ExpectedRoutes: TypeAlias = list["aws_sdk_fms.types.expected_route.ExpectedRoute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpectedRoutes) -> list:
    import aws_sdk_fms.types.expected_route

    out: list = []
    for item in value:
        out.append(aws_sdk_fms.types.expected_route.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExpectedRoutes:
    import aws_sdk_fms.types.expected_route

    out: ExpectedRoutes = []
    for item in data:
        out.append(aws_sdk_fms.types.expected_route.deserialize_aws_json_1_1(item))
    return out
