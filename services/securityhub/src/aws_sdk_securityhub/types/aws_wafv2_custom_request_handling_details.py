"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2CustomRequestHandlingDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_wafv2_insert_headers_list


class AwsWafv2CustomRequestHandlingDetails(TypedDict):
    insert_headers: NotRequired[
        "aws_sdk_securityhub.types.aws_wafv2_insert_headers_list.AwsWafv2InsertHeadersList"
    ]
    """<p> The HTTP headers to insert into the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2CustomRequestHandlingDetails) -> dict:
    out: dict = {}
    if "insert_headers" in value:
        import aws_sdk_securityhub.types.aws_wafv2_insert_headers_list

        out["InsertHeaders"] = (
            aws_sdk_securityhub.types.aws_wafv2_insert_headers_list.serialize_json(
                value["insert_headers"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafv2CustomRequestHandlingDetails:
    out: AwsWafv2CustomRequestHandlingDetails = {}  # type: ignore[typeddict-item]
    if "InsertHeaders" in data:
        import aws_sdk_securityhub.types.aws_wafv2_insert_headers_list

        out["insert_headers"] = (
            aws_sdk_securityhub.types.aws_wafv2_insert_headers_list.deserialize_json(
                data["InsertHeaders"]
            )
        )
    return out
