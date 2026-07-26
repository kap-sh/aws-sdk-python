"""Generated from Smithy shape ``com.amazonaws.redshift#NamespaceIdentifierUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_redshift._protocol.xml import Element
from capo_redshift.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_redshift.types.provisioned_identifier
    import capo_redshift.types.serverless_identifier


class _NamespaceIdentifierUnion_ServerlessIdentifier(TypedDict, closed=True):
    ServerlessIdentifier: (
        "capo_redshift.types.serverless_identifier.ServerlessIdentifier"
    )


class _NamespaceIdentifierUnion_ProvisionedIdentifier(TypedDict, closed=True):
    ProvisionedIdentifier: (
        "capo_redshift.types.provisioned_identifier.ProvisionedIdentifier"
    )


NamespaceIdentifierUnion: TypeAlias = (
    _NamespaceIdentifierUnion_ServerlessIdentifier
    | _NamespaceIdentifierUnion_ProvisionedIdentifier
)


# --- awsQuery ser/de ---
def serialize_query(
    value: NamespaceIdentifierUnion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ServerlessIdentifier" in value:
        import capo_redshift.types.serverless_identifier

        capo_redshift.types.serverless_identifier.serialize_query(
            value["ServerlessIdentifier"], pairs, f"{prefix}.ServerlessIdentifier"
        )
    elif "ProvisionedIdentifier" in value:
        import capo_redshift.types.provisioned_identifier

        capo_redshift.types.provisioned_identifier.serialize_query(
            value["ProvisionedIdentifier"], pairs, f"{prefix}.ProvisionedIdentifier"
        )
    else:
        raise SerializationError("NamespaceIdentifierUnion: no variant present")


def deserialize_query(el: Element) -> NamespaceIdentifierUnion:
    for child in el:
        if child.tag == "ServerlessIdentifier":
            import capo_redshift.types.serverless_identifier

            return {
                "ServerlessIdentifier": capo_redshift.types.serverless_identifier.deserialize_query(
                    child
                )
            }
        elif child.tag == "ProvisionedIdentifier":
            import capo_redshift.types.provisioned_identifier

            return {
                "ProvisionedIdentifier": capo_redshift.types.provisioned_identifier.deserialize_query(
                    child
                )
            }
    raise DeserializationError(
        "NamespaceIdentifierUnion: no recognized variant element"
    )
