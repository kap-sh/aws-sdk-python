"""Generated from Smithy shape ``com.amazonaws.appsync#DisassociateMergedGraphqlApiResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.source_api_association_status


class DisassociateMergedGraphqlApiResponse(TypedDict):
    source_api_association_status: NotRequired[
        "aws_sdk_appsync.types.source_api_association_status.SourceApiAssociationStatus"
    ]
    """<p>The state of the source API association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMergedGraphqlApiResponse) -> dict:
    out: dict = {}
    if "source_api_association_status" in value:
        import aws_sdk_appsync.types.source_api_association_status

        out["sourceApiAssociationStatus"] = (
            aws_sdk_appsync.types.source_api_association_status.serialize_json(
                value["source_api_association_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisassociateMergedGraphqlApiResponse:
    out: DisassociateMergedGraphqlApiResponse = {}  # type: ignore[typeddict-item]
    if "sourceApiAssociationStatus" in data:
        import aws_sdk_appsync.types.source_api_association_status

        out["source_api_association_status"] = (
            aws_sdk_appsync.types.source_api_association_status.deserialize_json(
                data["sourceApiAssociationStatus"]
            )
        )
    return out
