"""Generated from Smithy shape ``com.amazonaws.wafv2#CustomHTTPHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.custom_http_header

CustomHTTPHeaders: TypeAlias = list[
    "aws_sdk_wafv2.types.custom_http_header.CustomHTTPHeader"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomHTTPHeaders) -> list:
    import aws_sdk_wafv2.types.custom_http_header

    out: list = []
    for item in value:
        out.append(aws_sdk_wafv2.types.custom_http_header.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CustomHTTPHeaders:
    import aws_sdk_wafv2.types.custom_http_header

    out: CustomHTTPHeaders = []
    for item in data:
        out.append(
            aws_sdk_wafv2.types.custom_http_header.deserialize_aws_json_1_1(item)
        )
    return out
