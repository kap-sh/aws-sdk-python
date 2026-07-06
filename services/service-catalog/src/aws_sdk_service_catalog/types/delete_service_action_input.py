"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeleteServiceActionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.idempotency_token


class DeleteServiceActionInput(TypedDict, closed=True):
    id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The self-service action identifier. For example, <code>act-fs7abcd89wxyz</code>.</p>"""
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    idempotency_token: NotRequired[
        "aws_sdk_service_catalog.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique identifier that you provide to ensure idempotency. If multiple requests from the same Amazon Web Services account use the same idempotency token, the same response is returned for each repeated request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteServiceActionInput) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteServiceActionInput:
    out: DeleteServiceActionInput = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DeleteServiceActionInput.id required")
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
