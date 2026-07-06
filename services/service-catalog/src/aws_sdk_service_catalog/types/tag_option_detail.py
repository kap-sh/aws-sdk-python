"""Generated from Smithy shape ``com.amazonaws.servicecatalog#TagOptionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.owner
    import aws_sdk_service_catalog.types.tag_option_active
    import aws_sdk_service_catalog.types.tag_option_id
    import aws_sdk_service_catalog.types.tag_option_key
    import aws_sdk_service_catalog.types.tag_option_value


class TagOptionDetail(TypedDict, closed=True):
    key: NotRequired["aws_sdk_service_catalog.types.tag_option_key.TagOptionKey"]
    """<p>The TagOption key.</p>"""
    value: NotRequired["aws_sdk_service_catalog.types.tag_option_value.TagOptionValue"]
    """<p>The TagOption value.</p>"""
    active: NotRequired[
        "aws_sdk_service_catalog.types.tag_option_active.TagOptionActive"
    ]
    """<p>The TagOption active state.</p>"""
    id: NotRequired["aws_sdk_service_catalog.types.tag_option_id.TagOptionId"]
    """<p>The TagOption identifier.</p>"""
    owner: NotRequired["aws_sdk_service_catalog.types.owner.Owner"]
    """<p>The Amazon Web Services account Id of the owner account that created the TagOption.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagOptionDetail) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    if "active" in value:
        out["Active"] = value["active"]
    if "id" in value:
        out["Id"] = value["id"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TagOptionDetail:
    out: TagOptionDetail = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Active" in data:
        out["active"] = data["Active"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    return out
