"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkSchemaAndFacetName``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.typed_link_name


class TypedLinkSchemaAndFacetName(TypedDict):
    schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.</p>"""
    typed_link_name: "aws_sdk_clouddirectory.types.typed_link_name.TypedLinkName"
    """<p>The unique name of the typed link facet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TypedLinkSchemaAndFacetName) -> dict:
    out: dict = {}
    out["SchemaArn"] = value["schema_arn"]
    out["TypedLinkName"] = value["typed_link_name"]
    return out


def deserialize_json(data: dict) -> TypedLinkSchemaAndFacetName:
    out: TypedLinkSchemaAndFacetName = {}  # type: ignore[typeddict-item]
    if "SchemaArn" in data:
        out["schema_arn"] = data["SchemaArn"]
    else:
        raise DeserializationError("TypedLinkSchemaAndFacetName.schema_arn required")
    if "TypedLinkName" in data:
        out["typed_link_name"] = data["TypedLinkName"]
    else:
        raise DeserializationError(
            "TypedLinkSchemaAndFacetName.typed_link_name required"
        )
    return out
