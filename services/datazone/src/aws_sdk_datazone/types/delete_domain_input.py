"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteDomainInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id


class DeleteDomainInput(TypedDict):
    identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon Web Services domain that is to be deleted.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""
    skip_deletion_check: NotRequired["bool"]
    """<p>Specifies the optional flag to delete all child entities within the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainInput:
    out: DeleteDomainInput = {}  # type: ignore[typeddict-item]
    return out
