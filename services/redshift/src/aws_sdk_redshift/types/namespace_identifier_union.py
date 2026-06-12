"""Generated from Smithy shape ``com.amazonaws.redshift#NamespaceIdentifierUnion``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.provisioned_identifier
    import aws_sdk_redshift.types.serverless_identifier


class _NamespaceIdentifierUnion_ServerlessIdentifier(TypedDict):
    ServerlessIdentifier: (
        "aws_sdk_redshift.types.serverless_identifier.ServerlessIdentifier"
    )


class _NamespaceIdentifierUnion_ProvisionedIdentifier(TypedDict):
    ProvisionedIdentifier: (
        "aws_sdk_redshift.types.provisioned_identifier.ProvisionedIdentifier"
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
        import aws_sdk_redshift.types.serverless_identifier

        aws_sdk_redshift.types.serverless_identifier.serialize_query(
            value["ServerlessIdentifier"], pairs, f"{prefix}.ServerlessIdentifier"
        )
    elif "ProvisionedIdentifier" in value:
        import aws_sdk_redshift.types.provisioned_identifier

        aws_sdk_redshift.types.provisioned_identifier.serialize_query(
            value["ProvisionedIdentifier"], pairs, f"{prefix}.ProvisionedIdentifier"
        )
    else:
        raise SerializationError("NamespaceIdentifierUnion: no variant present")


def deserialize_query(el: Element) -> NamespaceIdentifierUnion:
    for child in el:
        if child.tag == "ServerlessIdentifier":
            import aws_sdk_redshift.types.serverless_identifier

            return {
                "ServerlessIdentifier": aws_sdk_redshift.types.serverless_identifier.deserialize_query(
                    child
                )
            }
        elif child.tag == "ProvisionedIdentifier":
            import aws_sdk_redshift.types.provisioned_identifier

            return {
                "ProvisionedIdentifier": aws_sdk_redshift.types.provisioned_identifier.deserialize_query(
                    child
                )
            }
    raise DeserializationError(
        "NamespaceIdentifierUnion: no recognized variant element"
    )
