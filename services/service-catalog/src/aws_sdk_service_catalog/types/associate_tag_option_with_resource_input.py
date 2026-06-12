"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AssociateTagOptionWithResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.resource_id
    import aws_sdk_service_catalog.types.tag_option_id


class AssociateTagOptionWithResourceInput(TypedDict):
    resource_id: "aws_sdk_service_catalog.types.resource_id.ResourceId"
    """<p>The resource identifier.</p>"""
    tag_option_id: "aws_sdk_service_catalog.types.tag_option_id.TagOptionId"
    """<p>The TagOption identifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateTagOptionWithResourceInput) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    out["TagOptionId"] = value["tag_option_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateTagOptionWithResourceInput:
    out: AssociateTagOptionWithResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "AssociateTagOptionWithResourceInput.resource_id required"
        )
    if "TagOptionId" in data:
        out["tag_option_id"] = data["TagOptionId"]
    else:
        raise DeserializationError(
            "AssociateTagOptionWithResourceInput.tag_option_id required"
        )
    return out
