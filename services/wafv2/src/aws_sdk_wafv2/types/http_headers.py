"""Generated from Smithy shape ``com.amazonaws.wafv2#HTTPHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.http_header

HTTPHeaders: TypeAlias = list["aws_sdk_wafv2.types.http_header.HTTPHeader"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HTTPHeaders) -> list:
    import aws_sdk_wafv2.types.http_header

    out: list = []
    for item in value:
        out.append(aws_sdk_wafv2.types.http_header.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> HTTPHeaders:
    import aws_sdk_wafv2.types.http_header

    out: HTTPHeaders = []
    for item in data:
        out.append(aws_sdk_wafv2.types.http_header.deserialize_aws_json_1_1(item))
    return out
