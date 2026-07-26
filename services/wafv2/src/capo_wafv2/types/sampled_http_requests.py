"""Generated from Smithy shape ``com.amazonaws.wafv2#SampledHTTPRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.sampled_http_request

SampledHTTPRequests: TypeAlias = list[
    "capo_wafv2.types.sampled_http_request.SampledHTTPRequest"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SampledHTTPRequests) -> list:
    import capo_wafv2.types.sampled_http_request

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.sampled_http_request.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SampledHTTPRequests:
    import capo_wafv2.types.sampled_http_request

    out: SampledHTTPRequests = []
    for item in data:
        out.append(capo_wafv2.types.sampled_http_request.deserialize_aws_json_1_1(item))
    return out
