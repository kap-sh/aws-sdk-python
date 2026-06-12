"""Generated from Smithy shape ``com.amazonaws.lightsail#HeaderObject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.forward_values
    import aws_sdk_lightsail.types.header_forward_list


class HeaderObject(TypedDict):
    option: NotRequired["aws_sdk_lightsail.types.forward_values.ForwardValues"]
    """<p>The headers that you want your distribution to forward to your origin and base caching on.</p> <p>You can configure your distribution to do one of the following:</p> <ul> <li> <p> <b> <code>all</code> </b> - Forward all headers to your origin.</p> </li> <li> <p> <b> <code>none</code> </b> - Forward only the default headers.</p> </li> <li> <p> <b> <code>allow-list</code> </b> - Forward only the headers you specify using the <code>headersAllowList</code> parameter.</p> </li> </ul>"""
    headers_allow_list: NotRequired[
        "aws_sdk_lightsail.types.header_forward_list.HeaderForwardList"
    ]
    """<p>The specific headers to forward to your distribution's origin.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HeaderObject) -> dict:
    out: dict = {}
    if "option" in value:
        import aws_sdk_lightsail.types.forward_values

        out["option"] = aws_sdk_lightsail.types.forward_values.serialize_aws_json_1_1(
            value["option"]
        )
    if "headers_allow_list" in value:
        import aws_sdk_lightsail.types.header_forward_list

        out["headersAllowList"] = (
            aws_sdk_lightsail.types.header_forward_list.serialize_aws_json_1_1(
                value["headers_allow_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HeaderObject:
    out: HeaderObject = {}  # type: ignore[typeddict-item]
    if "option" in data:
        import aws_sdk_lightsail.types.forward_values

        out["option"] = aws_sdk_lightsail.types.forward_values.deserialize_aws_json_1_1(
            data["option"]
        )
    if "headersAllowList" in data:
        import aws_sdk_lightsail.types.header_forward_list

        out["headers_allow_list"] = (
            aws_sdk_lightsail.types.header_forward_list.deserialize_aws_json_1_1(
                data["headersAllowList"]
            )
        )
    return out
