"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeletePortfolioInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id


class DeletePortfolioInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The portfolio identifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePortfolioInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePortfolioInput:
    out: DeletePortfolioInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DeletePortfolioInput.id required")
    return out
