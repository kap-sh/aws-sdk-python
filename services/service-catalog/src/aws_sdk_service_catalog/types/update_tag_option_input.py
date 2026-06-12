"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateTagOptionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.tag_option_active
    import aws_sdk_service_catalog.types.tag_option_id
    import aws_sdk_service_catalog.types.tag_option_value


class UpdateTagOptionInput(TypedDict):
    id: "aws_sdk_service_catalog.types.tag_option_id.TagOptionId"
    """<p>The TagOption identifier.</p>"""
    value: NotRequired["aws_sdk_service_catalog.types.tag_option_value.TagOptionValue"]
    """<p>The updated value.</p>"""
    active: NotRequired[
        "aws_sdk_service_catalog.types.tag_option_active.TagOptionActive"
    ]
    """<p>The updated active state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTagOptionInput) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "value" in value:
        out["Value"] = value["value"]
    if "active" in value:
        out["Active"] = value["active"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTagOptionInput:
    out: UpdateTagOptionInput = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateTagOptionInput.id required")
    if "Value" in data:
        out["value"] = data["Value"]
    if "Active" in data:
        out["active"] = data["Active"]
    return out
