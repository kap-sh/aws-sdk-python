"""Generated from Smithy shape ``com.amazonaws.amplify#UpdateDomainAssociationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.domain_association


class UpdateDomainAssociationResult(TypedDict, closed=True):
    domain_association: "capo_amplify.types.domain_association.DomainAssociation"
    """<p> Describes a domain association, which associates a custom domain with an Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainAssociationResult) -> dict:
    out: dict = {}
    import capo_amplify.types.domain_association

    out["domainAssociation"] = capo_amplify.types.domain_association.serialize_json(
        value["domain_association"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDomainAssociationResult:
    out: UpdateDomainAssociationResult = {}  # type: ignore[typeddict-item]
    if "domainAssociation" in data:
        import capo_amplify.types.domain_association

        out["domain_association"] = (
            capo_amplify.types.domain_association.deserialize_json(
                data["domainAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDomainAssociationResult.domain_association required"
        )
    return out
