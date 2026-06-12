"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2InsertHeadersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_wafv2_custom_http_header

AwsWafv2InsertHeadersList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_wafv2_custom_http_header.AwsWafv2CustomHttpHeader"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2InsertHeadersList) -> list:
    import aws_sdk_securityhub.types.aws_wafv2_custom_http_header

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_wafv2_custom_http_header.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsWafv2InsertHeadersList:
    import aws_sdk_securityhub.types.aws_wafv2_custom_http_header

    out: AwsWafv2InsertHeadersList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_wafv2_custom_http_header.deserialize_json(
                item
            )
        )
    return out
