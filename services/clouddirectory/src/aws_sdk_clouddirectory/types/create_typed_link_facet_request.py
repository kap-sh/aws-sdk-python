"""Generated from Smithy shape ``com.amazonaws.clouddirectory#CreateTypedLinkFacetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.typed_link_facet


class CreateTypedLinkFacetRequest(TypedDict, closed=True):
    schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.</p>"""
    facet: "aws_sdk_clouddirectory.types.typed_link_facet.TypedLinkFacet"
    """<p> <a>Facet</a> structure that is associated with the typed link facet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTypedLinkFacetRequest) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.typed_link_facet

    out["Facet"] = aws_sdk_clouddirectory.types.typed_link_facet.serialize_json(
        value["facet"]
    )
    return out


def deserialize_json(data: dict) -> CreateTypedLinkFacetRequest:
    out: CreateTypedLinkFacetRequest = {}  # type: ignore[typeddict-item]
    if "Facet" in data:
        import aws_sdk_clouddirectory.types.typed_link_facet

        out["facet"] = aws_sdk_clouddirectory.types.typed_link_facet.deserialize_json(
            data["Facet"]
        )
    else:
        raise DeserializationError("CreateTypedLinkFacetRequest.facet required")
    return out
