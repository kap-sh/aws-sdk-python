"""Generated from Smithy shape ``com.amazonaws.customerprofiles#PutDomainObjectTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.domain_object_type_fields
    import aws_sdk_customer_profiles.types.encryption_key
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.sensitive_string1_to10000
    import aws_sdk_customer_profiles.types.tag_map
    import aws_sdk_customer_profiles.types.type_name


class PutDomainObjectTypeRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    object_type_name: "aws_sdk_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the domain object type.</p>"""
    description: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to10000.sensitiveString1To10000"
    ]
    """<p>The description of the domain object type.</p>"""
    encryption_key: NotRequired[
        "aws_sdk_customer_profiles.types.encryption_key.encryptionKey"
    ]
    """<p>The customer provided KMS key used to encrypt this type of domain object.</p>"""
    fields: "aws_sdk_customer_profiles.types.domain_object_type_fields.DomainObjectTypeFields"
    """<p>A map of field names to their corresponding domain object type field definitions.</p>"""
    tags: NotRequired["aws_sdk_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDomainObjectTypeRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "encryption_key" in value:
        out["EncryptionKey"] = value["encryption_key"]
    import aws_sdk_customer_profiles.types.domain_object_type_fields

    out["Fields"] = (
        aws_sdk_customer_profiles.types.domain_object_type_fields.serialize_json(
            value["fields"]
        )
    )
    if "tags" in value:
        import aws_sdk_customer_profiles.types.tag_map

        out["Tags"] = aws_sdk_customer_profiles.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> PutDomainObjectTypeRequest:
    out: PutDomainObjectTypeRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EncryptionKey" in data:
        out["encryption_key"] = data["EncryptionKey"]
    if "Fields" in data:
        import aws_sdk_customer_profiles.types.domain_object_type_fields

        out["fields"] = (
            aws_sdk_customer_profiles.types.domain_object_type_fields.deserialize_json(
                data["Fields"]
            )
        )
    else:
        raise DeserializationError("PutDomainObjectTypeRequest.fields required")
    if "Tags" in data:
        import aws_sdk_customer_profiles.types.tag_map

        out["tags"] = aws_sdk_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
