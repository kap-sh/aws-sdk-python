"""Generated from Smithy shape ``com.amazonaws.appsync#GetSourceApiAssociationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.source_api_association


class GetSourceApiAssociationResponse(TypedDict):
    source_api_association: NotRequired[
        "aws_sdk_appsync.types.source_api_association.SourceApiAssociation"
    ]
    """<p>The <code>SourceApiAssociation</code> object data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSourceApiAssociationResponse) -> dict:
    out: dict = {}
    if "source_api_association" in value:
        import aws_sdk_appsync.types.source_api_association

        out["sourceApiAssociation"] = (
            aws_sdk_appsync.types.source_api_association.serialize_json(
                value["source_api_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSourceApiAssociationResponse:
    out: GetSourceApiAssociationResponse = {}  # type: ignore[typeddict-item]
    if "sourceApiAssociation" in data:
        import aws_sdk_appsync.types.source_api_association

        out["source_api_association"] = (
            aws_sdk_appsync.types.source_api_association.deserialize_json(
                data["sourceApiAssociation"]
            )
        )
    return out
