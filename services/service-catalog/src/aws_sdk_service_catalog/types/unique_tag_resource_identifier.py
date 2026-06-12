"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UniqueTagResourceIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.unique_tag_key
    import aws_sdk_service_catalog.types.unique_tag_value


class UniqueTagResourceIdentifier(TypedDict):
    key: NotRequired["aws_sdk_service_catalog.types.unique_tag_key.UniqueTagKey"]
    """<p> A unique key that's attached to a resource. </p>"""
    value: NotRequired["aws_sdk_service_catalog.types.unique_tag_value.UniqueTagValue"]
    """<p> A unique value that's attached to a resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UniqueTagResourceIdentifier) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UniqueTagResourceIdentifier:
    out: UniqueTagResourceIdentifier = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
