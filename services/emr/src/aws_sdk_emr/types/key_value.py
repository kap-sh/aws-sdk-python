"""Generated from Smithy shape ``com.amazonaws.emr#KeyValue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.xml_string


class KeyValue(TypedDict):
    key: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The unique identifier of a key-value pair.</p>"""
    value: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The value part of the identified key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyValue) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KeyValue:
    out: KeyValue = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
