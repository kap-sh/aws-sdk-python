"""Generated from Smithy shape ``com.amazonaws.firehose#HttpEndpointCommonAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.http_endpoint_attribute_name
    import aws_sdk_firehose.types.http_endpoint_attribute_value


class HttpEndpointCommonAttribute(TypedDict):
    attribute_name: (
        "aws_sdk_firehose.types.http_endpoint_attribute_name.HttpEndpointAttributeName"
    )
    """<p>The name of the HTTP endpoint common attribute.</p>"""
    attribute_value: "aws_sdk_firehose.types.http_endpoint_attribute_value.HttpEndpointAttributeValue"
    """<p>The value of the HTTP endpoint common attribute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpEndpointCommonAttribute) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    out["AttributeValue"] = value["attribute_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpEndpointCommonAttribute:
    out: HttpEndpointCommonAttribute = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError(
            "HttpEndpointCommonAttribute.attribute_name required"
        )
    if "AttributeValue" in data:
        out["attribute_value"] = data["AttributeValue"]
    else:
        raise DeserializationError(
            "HttpEndpointCommonAttribute.attribute_value required"
        )
    return out
