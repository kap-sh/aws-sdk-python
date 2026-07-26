"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateTagOptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.tag_option_key
    import capo_service_catalog.types.tag_option_value


class CreateTagOptionInput(TypedDict, closed=True):
    key: "capo_service_catalog.types.tag_option_key.TagOptionKey"
    """<p>The TagOption key.</p>"""
    value: "capo_service_catalog.types.tag_option_value.TagOptionValue"
    """<p>The TagOption value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTagOptionInput) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTagOptionInput:
    out: CreateTagOptionInput = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("CreateTagOptionInput.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("CreateTagOptionInput.value required")
    return out
