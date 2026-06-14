"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssociateAwsAccountWithPartnerAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.client_request_token
    import aws_sdk_iot_wireless.types.sidewalk_account_info
    import aws_sdk_iot_wireless.types.tag_list


class AssociateAwsAccountWithPartnerAccountRequest(TypedDict):
    sidewalk: "aws_sdk_iot_wireless.types.sidewalk_account_info.SidewalkAccountInfo"
    """<p>The Sidewalk account credentials.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_iot_wireless.types.client_request_token.ClientRequestToken"
    ]
    r"""<p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a>.</p>"""
    tags: NotRequired["aws_sdk_iot_wireless.types.tag_list.TagList"]
    """<p>The tags to attach to the specified resource. Tags are metadata that you can use to manage a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAwsAccountWithPartnerAccountRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_wireless.types.sidewalk_account_info

    out["Sidewalk"] = aws_sdk_iot_wireless.types.sidewalk_account_info.serialize_json(
        value["sidewalk"]
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import aws_sdk_iot_wireless.types.tag_list

        out["Tags"] = aws_sdk_iot_wireless.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssociateAwsAccountWithPartnerAccountRequest:
    out: AssociateAwsAccountWithPartnerAccountRequest = {}  # type: ignore[typeddict-item]
    if "Sidewalk" in data:
        import aws_sdk_iot_wireless.types.sidewalk_account_info

        out["sidewalk"] = (
            aws_sdk_iot_wireless.types.sidewalk_account_info.deserialize_json(
                data["Sidewalk"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateAwsAccountWithPartnerAccountRequest.sidewalk required"
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Tags" in data:
        import aws_sdk_iot_wireless.types.tag_list

        out["tags"] = aws_sdk_iot_wireless.types.tag_list.deserialize_json(data["Tags"])
    return out
