"""Generated from Smithy shape ``com.amazonaws.wafregional#HTTPHeaders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf_regional.types.http_header

HTTPHeaders: TypeAlias = list["capo_waf_regional.types.http_header.HTTPHeader"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HTTPHeaders) -> list:
    import capo_waf_regional.types.http_header

    out: list = []
    for item in value:
        out.append(capo_waf_regional.types.http_header.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> HTTPHeaders:
    import capo_waf_regional.types.http_header

    out: HTTPHeaders = []
    for item in data:
        out.append(capo_waf_regional.types.http_header.deserialize_aws_json_1_1(item))
    return out
