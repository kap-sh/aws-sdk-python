"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ObjectTypeField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.field_content_type
    import aws_sdk_customer_profiles.types.text


class ObjectTypeField(TypedDict, closed=True):
    source: NotRequired["aws_sdk_customer_profiles.types.text.text"]
    """<p>A field of a ProfileObject. For example: _source.FirstName, where “_source” is a ProfileObjectType of a Zendesk user and “FirstName” is a field in that ObjectType.</p>"""
    target: NotRequired["aws_sdk_customer_profiles.types.text.text"]
    """<p>The location of the data in the standard ProfileObject model. For example: _profile.Address.PostalCode. Do not include sensitive or personally identifiable information (PII) in the target field name.</p>"""
    content_type: NotRequired[
        "aws_sdk_customer_profiles.types.field_content_type.FieldContentType"
    ]
    """<p>The content type of the field. Used for determining equality when searching.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectTypeField) -> dict:
    out: dict = {}
    if "source" in value:
        out["Source"] = value["source"]
    if "target" in value:
        out["Target"] = value["target"]
    if "content_type" in value:
        import aws_sdk_customer_profiles.types.field_content_type

        out["ContentType"] = (
            aws_sdk_customer_profiles.types.field_content_type.serialize_json(
                value["content_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ObjectTypeField:
    out: ObjectTypeField = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        out["source"] = data["Source"]
    if "Target" in data:
        out["target"] = data["Target"]
    if "ContentType" in data:
        import aws_sdk_customer_profiles.types.field_content_type

        out["content_type"] = (
            aws_sdk_customer_profiles.types.field_content_type.deserialize_json(
                data["ContentType"]
            )
        )
    return out
