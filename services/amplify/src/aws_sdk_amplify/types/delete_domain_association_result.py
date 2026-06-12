"""Generated from Smithy shape ``com.amazonaws.amplify#DeleteDomainAssociationResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.domain_association


class DeleteDomainAssociationResult(TypedDict):
    domain_association: "aws_sdk_amplify.types.domain_association.DomainAssociation"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainAssociationResult) -> dict:
    out: dict = {}
    import aws_sdk_amplify.types.domain_association

    out["domainAssociation"] = aws_sdk_amplify.types.domain_association.serialize_json(
        value["domain_association"]
    )
    return out


def deserialize_json(data: dict) -> DeleteDomainAssociationResult:
    out: DeleteDomainAssociationResult = {}  # type: ignore[typeddict-item]
    if "domainAssociation" in data:
        import aws_sdk_amplify.types.domain_association

        out["domain_association"] = (
            aws_sdk_amplify.types.domain_association.deserialize_json(
                data["domainAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteDomainAssociationResult.domain_association required"
        )
    return out
