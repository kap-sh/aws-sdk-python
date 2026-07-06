"""Generated from Smithy shape ``com.amazonaws.sns#CreatePlatformEndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.map_string_to_string
    import aws_sdk_sns.types.string


class CreatePlatformEndpointInput(TypedDict, closed=True):
    platform_application_arn: "aws_sdk_sns.types.string.String"
    """<p> <code>PlatformApplicationArn</code> returned from CreatePlatformApplication is used to create a an endpoint.</p>"""
    token: "aws_sdk_sns.types.string.String"
    """<p>Unique identifier created by the notification service for an app on a device. The specific name for Token will vary, depending on which notification service is being used. For example, when using APNS as the notification service, you need the device token. Alternatively, when using GCM (Firebase Cloud Messaging) or ADM, the device token equivalent is called the registration ID.</p>"""
    custom_user_data: NotRequired["aws_sdk_sns.types.string.String"]
    """<p>Arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.</p>"""
    attributes: NotRequired["aws_sdk_sns.types.map_string_to_string.MapStringToString"]
    r"""<p>For a list of attributes, see <a href=\"https://docs.aws.amazon.com/sns/latest/api/API_SetEndpointAttributes.html\"> <code>SetEndpointAttributes</code> </a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreatePlatformEndpointInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append(
        (f"{prefix}.PlatformApplicationArn", str(value["platform_application_arn"]))
    )
    pairs.append((f"{prefix}.Token", str(value["token"])))
    if "custom_user_data" in value:
        pairs.append((f"{prefix}.CustomUserData", str(value["custom_user_data"])))
    if "attributes" in value:
        import aws_sdk_sns.types.map_string_to_string

        aws_sdk_sns.types.map_string_to_string.serialize_query(
            value["attributes"], pairs, f"{prefix}.Attributes"
        )


def deserialize_query(el: Element) -> CreatePlatformEndpointInput:
    out: CreatePlatformEndpointInput = {}  # type: ignore[typeddict-item]
    child_platform_application_arn = el.find("PlatformApplicationArn")
    if child_platform_application_arn is not None:
        out["platform_application_arn"] = str(child_platform_application_arn.text or "")
    else:
        raise DeserializationError(
            "CreatePlatformEndpointInput.platform_application_arn required"
        )
    child_token = el.find("Token")
    if child_token is not None:
        out["token"] = str(child_token.text or "")
    else:
        raise DeserializationError("CreatePlatformEndpointInput.token required")
    child_custom_user_data = el.find("CustomUserData")
    if child_custom_user_data is not None:
        out["custom_user_data"] = str(child_custom_user_data.text or "")
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import aws_sdk_sns.types.map_string_to_string

        out["attributes"] = aws_sdk_sns.types.map_string_to_string.deserialize_query(
            child_attributes
        )
    return out
