"""Generated from Smithy shape ``com.amazonaws.entityresolution#SchemaInputAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.attribute_name
    import aws_sdk_entityresolution.types.schema_attribute_type


class SchemaInputAttribute(TypedDict):
    field_name: "aws_sdk_entityresolution.types.attribute_name.AttributeName"
    """<p>A string containing the field name.</p>"""
    type: "aws_sdk_entityresolution.types.schema_attribute_type.SchemaAttributeType"
    """<p>The type of the attribute, selected from a list of values.</p> <p>LiveRamp supports: <code>NAME</code> | <code>NAME_FIRST</code> | <code>NAME_MIDDLE</code> | <code>NAME_LAST</code> | <code>ADDRESS</code> | <code>ADDRESS_STREET1</code> | <code>ADDRESS_STREET2</code> | <code>ADDRESS_STREET3</code> | <code>ADDRESS_CITY</code> | <code>ADDRESS_STATE</code> | <code>ADDRESS_COUNTRY</code> | <code>ADDRESS_POSTALCODE</code> | <code>PHONE</code> | <code>PHONE_NUMBER</code> | <code>EMAIL_ADDRESS</code> | <code>UNIQUE_ID</code> | <code>PROVIDER_ID</code> </p> <p>TransUnion supports: <code>NAME</code> | <code>NAME_FIRST</code> | <code>NAME_LAST</code> | <code>ADDRESS</code> | <code>ADDRESS_CITY</code> | <code>ADDRESS_STATE</code> | <code>ADDRESS_COUNTRY</code> | <code>ADDRESS_POSTALCODE</code> | <code>PHONE_NUMBER</code> | <code>EMAIL_ADDRESS</code> | <code>UNIQUE_ID</code> | <code>IPV4</code> | <code>IPV6</code> | <code>MAID</code> </p> <p>Unified ID 2.0 supports: <code>PHONE_NUMBER</code> | <code>EMAIL_ADDRESS</code> | <code>UNIQUE_ID</code> </p> <note> <p>Normalization is only supported for <code>NAME</code>, <code>ADDRESS</code>, <code>PHONE</code>, and <code>EMAIL_ADDRESS</code>. </p> <p>If you want to normalize <code>NAME_FIRST</code>, <code>NAME_MIDDLE</code>, and <code>NAME_LAST</code>, you must group them by assigning them to the <code>NAME</code> <code>groupName</code>. </p> <p>If you want to normalize <code>ADDRESS_STREET1</code>, <code>ADDRESS_STREET2</code>, <code>ADDRESS_STREET3</code>, <code>ADDRESS_CITY</code>, <code>ADDRESS_STATE</code>, <code>ADDRESS_COUNTRY</code>, and <code>ADDRESS_POSTALCODE</code>, you must group them by assigning them to the <code>ADDRESS</code> <code>groupName</code>. </p> <p>If you want to normalize <code>PHONE_NUMBER</code> and <code>PHONE_COUNTRYCODE</code>, you must group them by assigning them to the <code>PHONE</code> <code>groupName</code>. </p> </note>"""
    group_name: NotRequired[
        "aws_sdk_entityresolution.types.attribute_name.AttributeName"
    ]
    """<p>A string that instructs Entity Resolution to combine several columns into a unified column with the identical attribute type. </p> <p>For example, when working with columns such as <code>NAME_FIRST</code>, <code>NAME_MIDDLE</code>, and <code>NAME_LAST</code>, assigning them a common <code>groupName</code> will prompt Entity Resolution to concatenate them into a single value.</p>"""
    match_key: NotRequired[
        "aws_sdk_entityresolution.types.attribute_name.AttributeName"
    ]
    """<p>A key that allows grouping of multiple input attributes into a unified matching group. </p> <p>For example, consider a scenario where the source table contains various addresses, such as <code>business_address</code> and <code>shipping_address</code>. By assigning a <code>matchKey</code> called <code>address</code> to both attributes, Entity Resolution will match records across these fields to create a consolidated matching group.</p> <p>If no <code>matchKey</code> is specified for a column, it won't be utilized for matching purposes but will still be included in the output table.</p>"""
    sub_type: NotRequired["aws_sdk_entityresolution.types.attribute_name.AttributeName"]
    """<p>The subtype of the attribute, selected from a list of values.</p>"""
    hashed: NotRequired["bool"]
    """<p> Indicates if the column values are hashed in the schema input. </p> <p>If the value is set to <code>TRUE</code>, the column values are hashed. </p> <p>If the value is set to <code>FALSE</code>, the column values are cleartext.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaInputAttribute) -> dict:
    out: dict = {}
    out["fieldName"] = value["field_name"]
    import aws_sdk_entityresolution.types.schema_attribute_type

    out["type"] = aws_sdk_entityresolution.types.schema_attribute_type.serialize_json(
        value["type"]
    )
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    if "match_key" in value:
        out["matchKey"] = value["match_key"]
    if "sub_type" in value:
        out["subType"] = value["sub_type"]
    if "hashed" in value:
        out["hashed"] = value["hashed"]
    return out


def deserialize_json(data: dict) -> SchemaInputAttribute:
    out: SchemaInputAttribute = {}  # type: ignore[typeddict-item]
    if "fieldName" in data:
        out["field_name"] = data["fieldName"]
    else:
        raise DeserializationError("SchemaInputAttribute.field_name required")
    if "type" in data:
        import aws_sdk_entityresolution.types.schema_attribute_type

        out["type"] = (
            aws_sdk_entityresolution.types.schema_attribute_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("SchemaInputAttribute.type required")
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    if "matchKey" in data:
        out["match_key"] = data["matchKey"]
    if "subType" in data:
        out["sub_type"] = data["subType"]
    if "hashed" in data:
        out["hashed"] = data["hashed"]
    return out
