"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetObjectInformationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.object_identifier
    import aws_sdk_clouddirectory.types.schema_facet_list


class GetObjectInformationResponse(TypedDict):
    schema_facets: NotRequired[
        "aws_sdk_clouddirectory.types.schema_facet_list.SchemaFacetList"
    ]
    """<p>The facets attached to the specified object. Although the response does not include minor version information, the most recently applied minor version of each Facet is in effect. See <a>GetAppliedSchemaVersion</a> for details.</p>"""
    object_identifier: NotRequired[
        "aws_sdk_clouddirectory.types.object_identifier.ObjectIdentifier"
    ]
    """<p>The <code>ObjectIdentifier</code> of the specified object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetObjectInformationResponse) -> dict:
    out: dict = {}
    if "schema_facets" in value:
        import aws_sdk_clouddirectory.types.schema_facet_list

        out["SchemaFacets"] = (
            aws_sdk_clouddirectory.types.schema_facet_list.serialize_json(
                value["schema_facets"]
            )
        )
    if "object_identifier" in value:
        out["ObjectIdentifier"] = value["object_identifier"]
    return out


def deserialize_json(data: dict) -> GetObjectInformationResponse:
    out: GetObjectInformationResponse = {}  # type: ignore[typeddict-item]
    if "SchemaFacets" in data:
        import aws_sdk_clouddirectory.types.schema_facet_list

        out["schema_facets"] = (
            aws_sdk_clouddirectory.types.schema_facet_list.deserialize_json(
                data["SchemaFacets"]
            )
        )
    if "ObjectIdentifier" in data:
        out["object_identifier"] = data["ObjectIdentifier"]
    return out
