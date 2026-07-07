"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderSchemaAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.attribute_name
    import aws_sdk_entityresolution.types.schema_attribute_type


class ProviderSchemaAttribute(TypedDict, closed=True):
    field_name: "aws_sdk_entityresolution.types.attribute_name.AttributeName"
    """<p>The field name.</p>"""
    type: "aws_sdk_entityresolution.types.schema_attribute_type.SchemaAttributeType"
    """<p>The type of the provider schema attribute.</p> <p>LiveRamp supports: <code>NAME</code> | <code>NAME_FIRST</code> | <code>NAME_MIDDLE</code> | <code>NAME_LAST</code> | <code>ADDRESS</code> | <code>ADDRESS_STREET1</code> | <code>ADDRESS_STREET2</code> | <code>ADDRESS_STREET3</code> | <code>ADDRESS_CITY</code> | <code>ADDRESS_STATE</code> | <code>ADDRESS_COUNTRY</code> | <code>ADDRESS_POSTALCODE</code> | <code>PHONE</code> | <code>PHONE_NUMBER</code> | <code>EMAIL_ADDRESS</code> | <code>UNIQUE_ID</code> | <code>PROVIDER_ID</code> </p> <p>TransUnion supports: <code>NAME</code> | <code>NAME_FIRST</code> | <code>NAME_LAST</code> | <code>ADDRESS</code> | <code>ADDRESS_CITY</code> | <code>ADDRESS_STATE</code> | <code>ADDRESS_COUNTRY</code> | <code>ADDRESS_POSTALCODE</code> | <code>PHONE_NUMBER</code> | <code>EMAIL_ADDRESS</code> | <code>UNIQUE_ID</code> | <code>DATE</code> | <code>IPV4</code> | <code>IPV6</code> | <code>MAID</code> </p> <p>Unified ID 2.0 supports: <code>PHONE_NUMBER</code> | <code>EMAIL_ADDRESS</code> | <code>UNIQUE_ID</code> </p>"""
    sub_type: NotRequired["aws_sdk_entityresolution.types.attribute_name.AttributeName"]
    """<p>The sub type of the provider schema attribute.</p>"""
    hashing: NotRequired["bool"]
    """<p>The hashing attribute of the provider schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProviderSchemaAttribute) -> dict:
    out: dict = {}
    out["fieldName"] = value["field_name"]
    import aws_sdk_entityresolution.types.schema_attribute_type

    out["type"] = aws_sdk_entityresolution.types.schema_attribute_type.serialize_json(
        value["type"]
    )
    if "sub_type" in value:
        out["subType"] = value["sub_type"]
    if "hashing" in value:
        out["hashing"] = value["hashing"]
    return out


def deserialize_json(data: dict) -> ProviderSchemaAttribute:
    out: ProviderSchemaAttribute = {}  # type: ignore[typeddict-item]
    if "fieldName" in data:
        out["field_name"] = data["fieldName"]
    else:
        raise DeserializationError("ProviderSchemaAttribute.field_name required")
    if "type" in data:
        import aws_sdk_entityresolution.types.schema_attribute_type

        out["type"] = (
            aws_sdk_entityresolution.types.schema_attribute_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("ProviderSchemaAttribute.type required")
    if "subType" in data:
        out["sub_type"] = data["subType"]
    if "hashing" in data:
        out["hashing"] = data["hashing"]
    return out
