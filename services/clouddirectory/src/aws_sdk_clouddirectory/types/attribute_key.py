"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttributeKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.attribute_name
    import aws_sdk_clouddirectory.types.facet_name


class AttributeKey(TypedDict, closed=True):
    schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the schema that contains the facet and attribute.</p>"""
    facet_name: "aws_sdk_clouddirectory.types.facet_name.FacetName"
    """<p>The name of the facet that the attribute exists within.</p>"""
    name: "aws_sdk_clouddirectory.types.attribute_name.AttributeName"
    """<p>The name of the attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeKey) -> dict:
    out: dict = {}
    out["SchemaArn"] = value["schema_arn"]
    out["FacetName"] = value["facet_name"]
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AttributeKey:
    out: AttributeKey = {}  # type: ignore[typeddict-item]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    else:
        raise DeserializationError("AttributeKey.schema_arn required")
    if "FacetName" in data:
        out["facet_name"] = data["FacetName"]
    else:
        raise DeserializationError("AttributeKey.facet_name required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("AttributeKey.name required")
    return out
