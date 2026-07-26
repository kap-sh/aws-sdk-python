"""Generated from Smithy shape ``com.amazonaws.amplify#DeleteDomainAssociationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.domain_association


class DeleteDomainAssociationResult(TypedDict, closed=True):
    domain_association: "capo_amplify.types.domain_association.DomainAssociation"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainAssociationResult) -> dict:
    out: dict = {}
    import capo_amplify.types.domain_association

    out["domainAssociation"] = capo_amplify.types.domain_association.serialize_json(
        value["domain_association"]
    )
    return out


def deserialize_json(data: dict) -> DeleteDomainAssociationResult:
    out: DeleteDomainAssociationResult = {}  # type: ignore[typeddict-item]
    if "domainAssociation" in data:
        import capo_amplify.types.domain_association

        out["domain_association"] = (
            capo_amplify.types.domain_association.deserialize_json(
                data["domainAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteDomainAssociationResult.domain_association required"
        )
    return out
