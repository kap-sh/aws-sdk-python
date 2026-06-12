"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DeleteFacetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.facet_name


class DeleteFacetRequest(TypedDict):
    schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Facet</a>. For more information, see <a>arns</a>.</p>"""
    name: "aws_sdk_clouddirectory.types.facet_name.FacetName"
    """<p>The name of the facet to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFacetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteFacetRequest:
    out: DeleteFacetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteFacetRequest.name required")
    return out
