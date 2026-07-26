"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkSchemaAndFacetName``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.typed_link_name


class TypedLinkSchemaAndFacetName(TypedDict, closed=True):
    schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.</p>"""
    typed_link_name: "capo_clouddirectory.types.typed_link_name.TypedLinkName"
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
