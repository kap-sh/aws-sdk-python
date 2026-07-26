"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2CustomRequestHandlingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_wafv2_insert_headers_list


class AwsWafv2CustomRequestHandlingDetails(TypedDict, closed=True):
    insert_headers: NotRequired[
        "capo_securityhub.types.aws_wafv2_insert_headers_list.AwsWafv2InsertHeadersList"
    ]
    """<p> The HTTP headers to insert into the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2CustomRequestHandlingDetails) -> dict:
    out: dict = {}
    if "insert_headers" in value:
        import capo_securityhub.types.aws_wafv2_insert_headers_list

        out["InsertHeaders"] = (
            capo_securityhub.types.aws_wafv2_insert_headers_list.serialize_json(
                value["insert_headers"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafv2CustomRequestHandlingDetails:
    out: AwsWafv2CustomRequestHandlingDetails = {}  # type: ignore[typeddict-item]
    if "InsertHeaders" in data:
        import capo_securityhub.types.aws_wafv2_insert_headers_list

        out["insert_headers"] = (
            capo_securityhub.types.aws_wafv2_insert_headers_list.deserialize_json(
                data["InsertHeaders"]
            )
        )
    return out
