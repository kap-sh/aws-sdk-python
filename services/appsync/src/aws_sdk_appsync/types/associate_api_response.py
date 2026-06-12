"""Generated from Smithy shape ``com.amazonaws.appsync#AssociateApiResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.api_association


class AssociateApiResponse(TypedDict):
    api_association: NotRequired["aws_sdk_appsync.types.api_association.ApiAssociation"]
    """<p>The <code>ApiAssociation</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateApiResponse) -> dict:
    out: dict = {}
    if "api_association" in value:
        import aws_sdk_appsync.types.api_association

        out["apiAssociation"] = aws_sdk_appsync.types.api_association.serialize_json(
            value["api_association"]
        )
    return out


def deserialize_json(data: dict) -> AssociateApiResponse:
    out: AssociateApiResponse = {}  # type: ignore[typeddict-item]
    if "apiAssociation" in data:
        import aws_sdk_appsync.types.api_association

        out["api_association"] = aws_sdk_appsync.types.api_association.deserialize_json(
            data["apiAssociation"]
        )
    return out
