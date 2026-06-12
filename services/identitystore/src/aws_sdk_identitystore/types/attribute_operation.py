"""Generated from Smithy shape ``com.amazonaws.identitystore#AttributeOperation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.attribute_path
    import aws_sdk_identitystore.types.attribute_value


class AttributeOperation(TypedDict):
    attribute_path: "aws_sdk_identitystore.types.attribute_path.AttributePath"
    """<p>A string representation of the path to a given attribute or sub-attribute. Supports JMESPath.</p>"""
    attribute_value: NotRequired[
        "aws_sdk_identitystore.types.attribute_value.AttributeValue"
    ]
    """<p>The value of the attribute. This is a <code>Document</code> type. This type is not supported by Java V1, Go V1, and older versions of the CLI.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeOperation) -> dict:
    out: dict = {}
    out["AttributePath"] = value["attribute_path"]
    if "attribute_value" in value:
        out["AttributeValue"] = value["attribute_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttributeOperation:
    out: AttributeOperation = {}  # type: ignore[typeddict-item]
    if "AttributePath" in data:
        out["attribute_path"] = data["AttributePath"]
    else:
        raise DeserializationError("AttributeOperation.attribute_path required")
    if "AttributeValue" in data:
        out["attribute_value"] = data["AttributeValue"]
    return out
