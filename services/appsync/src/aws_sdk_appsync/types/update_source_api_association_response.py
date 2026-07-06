"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateSourceApiAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.source_api_association


class UpdateSourceApiAssociationResponse(TypedDict, closed=True):
    source_api_association: NotRequired[
        "aws_sdk_appsync.types.source_api_association.SourceApiAssociation"
    ]
    """<p>The <code>SourceApiAssociation</code> object data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSourceApiAssociationResponse) -> dict:
    out: dict = {}
    if "source_api_association" in value:
        import aws_sdk_appsync.types.source_api_association

        out["sourceApiAssociation"] = (
            aws_sdk_appsync.types.source_api_association.serialize_json(
                value["source_api_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSourceApiAssociationResponse:
    out: UpdateSourceApiAssociationResponse = {}  # type: ignore[typeddict-item]
    if "sourceApiAssociation" in data:
        import aws_sdk_appsync.types.source_api_association

        out["source_api_association"] = (
            aws_sdk_appsync.types.source_api_association.deserialize_json(
                data["sourceApiAssociation"]
            )
        )
    return out
