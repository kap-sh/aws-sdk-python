"""Generated from Smithy shape ``com.amazonaws.redshift#RegisterNamespaceInputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.consumer_identifier_list
    import capo_redshift.types.namespace_identifier_union


class RegisterNamespaceInputMessage(TypedDict, closed=True):
    namespace_identifier: NotRequired[
        "capo_redshift.types.namespace_identifier_union.NamespaceIdentifierUnion"
    ]
    """<p>The unique identifier of the cluster or serverless namespace that you want to register. </p>"""
    consumer_identifiers: NotRequired[
        "capo_redshift.types.consumer_identifier_list.ConsumerIdentifierList"
    ]
    """<p>An array containing the ID of the consumer account that you want to register the namespace to.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RegisterNamespaceInputMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "namespace_identifier" in value:
        import capo_redshift.types.namespace_identifier_union

        capo_redshift.types.namespace_identifier_union.serialize_query(
            value["namespace_identifier"], pairs, f"{key_prefix}NamespaceIdentifier"
        )
    if "consumer_identifiers" in value:
        import capo_redshift.types.consumer_identifier_list

        capo_redshift.types.consumer_identifier_list.serialize_query(
            value["consumer_identifiers"], pairs, f"{key_prefix}ConsumerIdentifiers"
        )


def deserialize_query(el: Element) -> RegisterNamespaceInputMessage:
    out: RegisterNamespaceInputMessage = {}  # type: ignore[typeddict-item]
    child_namespace_identifier = el.find("NamespaceIdentifier")
    if child_namespace_identifier is not None:
        import capo_redshift.types.namespace_identifier_union

        out["namespace_identifier"] = (
            capo_redshift.types.namespace_identifier_union.deserialize_query(
                child_namespace_identifier
            )
        )
    child_consumer_identifiers = el.find("ConsumerIdentifiers")
    if child_consumer_identifiers is not None:
        import capo_redshift.types.consumer_identifier_list

        out["consumer_identifiers"] = (
            capo_redshift.types.consumer_identifier_list.deserialize_query(
                child_consumer_identifiers
            )
        )
    return out
