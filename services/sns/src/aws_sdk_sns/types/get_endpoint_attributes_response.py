"""Generated from Smithy shape ``com.amazonaws.sns#GetEndpointAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.map_string_to_string


class GetEndpointAttributesResponse(TypedDict, closed=True):
    attributes: NotRequired["aws_sdk_sns.types.map_string_to_string.MapStringToString"]
    """<p>Attributes include the following:</p> <ul> <li> <p> <code>CustomUserData</code> – arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.</p> </li> <li> <p> <code>Enabled</code> – flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token.</p> </li> <li> <p> <code>Token</code> – device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.</p> <note> <p>The device token for the iOS platform is returned in lowercase.</p> </note> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetEndpointAttributesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "attributes" in value:
        import aws_sdk_sns.types.map_string_to_string

        aws_sdk_sns.types.map_string_to_string.serialize_query(
            value["attributes"], pairs, f"{prefix}.Attributes"
        )


def deserialize_query(el: Element) -> GetEndpointAttributesResponse:
    out: GetEndpointAttributesResponse = {}  # type: ignore[typeddict-item]
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import aws_sdk_sns.types.map_string_to_string

        out["attributes"] = aws_sdk_sns.types.map_string_to_string.deserialize_query(
            child_attributes
        )
    return out
