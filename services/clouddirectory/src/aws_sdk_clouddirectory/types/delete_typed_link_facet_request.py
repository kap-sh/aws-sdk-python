"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DeleteTypedLinkFacetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.typed_link_name


class DeleteTypedLinkFacetRequest(TypedDict, closed=True):
    schema_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the schema. For more information, see <a>arns</a>.</p>"""
    name: "aws_sdk_clouddirectory.types.typed_link_name.TypedLinkName"
    """<p>The unique name of the typed link facet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTypedLinkFacetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteTypedLinkFacetRequest:
    out: DeleteTypedLinkFacetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteTypedLinkFacetRequest.name required")
    return out
