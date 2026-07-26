"""Generated from Smithy shape ``com.amazonaws.amplify#ListDomainAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.domain_associations
    import capo_amplify.types.next_token


class ListDomainAssociationsResult(TypedDict, closed=True):
    domain_associations: "capo_amplify.types.domain_associations.DomainAssociations"
    """<p> A list of domain associations. </p>"""
    next_token: NotRequired["capo_amplify.types.next_token.NextToken"]
    """<p> A pagination token. If non-null, a pagination token is returned in a result. Pass its value in another request to retrieve more entries. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainAssociationsResult) -> dict:
    out: dict = {}
    import capo_amplify.types.domain_associations

    out["domainAssociations"] = capo_amplify.types.domain_associations.serialize_json(
        value["domain_associations"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainAssociationsResult:
    out: ListDomainAssociationsResult = {}  # type: ignore[typeddict-item]
    if "domainAssociations" in data:
        import capo_amplify.types.domain_associations

        out["domain_associations"] = (
            capo_amplify.types.domain_associations.deserialize_json(
                data["domainAssociations"]
            )
        )
    else:
        raise DeserializationError(
            "ListDomainAssociationsResult.domain_associations required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
