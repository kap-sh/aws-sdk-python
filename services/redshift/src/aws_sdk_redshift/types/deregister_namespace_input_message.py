"""Generated from Smithy shape ``com.amazonaws.redshift#DeregisterNamespaceInputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.consumer_identifier_list
    import aws_sdk_redshift.types.namespace_identifier_union


class DeregisterNamespaceInputMessage(TypedDict, closed=True):
    namespace_identifier: NotRequired[
        "aws_sdk_redshift.types.namespace_identifier_union.NamespaceIdentifierUnion"
    ]
    """<p>The unique identifier of the cluster or serverless namespace that you want to deregister.</p>"""
    consumer_identifiers: NotRequired[
        "aws_sdk_redshift.types.consumer_identifier_list.ConsumerIdentifierList"
    ]
    """<p>An array containing the ID of the consumer account that you want to deregister the cluster or serverless namespace from.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeregisterNamespaceInputMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "namespace_identifier" in value:
        import aws_sdk_redshift.types.namespace_identifier_union

        aws_sdk_redshift.types.namespace_identifier_union.serialize_query(
            value["namespace_identifier"], pairs, f"{prefix}.NamespaceIdentifier"
        )
    if "consumer_identifiers" in value:
        import aws_sdk_redshift.types.consumer_identifier_list

        aws_sdk_redshift.types.consumer_identifier_list.serialize_query(
            value["consumer_identifiers"], pairs, f"{prefix}.ConsumerIdentifiers"
        )


def deserialize_query(el: Element) -> DeregisterNamespaceInputMessage:
    out: DeregisterNamespaceInputMessage = {}  # type: ignore[typeddict-item]
    child_namespace_identifier = el.find("NamespaceIdentifier")
    if child_namespace_identifier is not None:
        import aws_sdk_redshift.types.namespace_identifier_union

        out["namespace_identifier"] = (
            aws_sdk_redshift.types.namespace_identifier_union.deserialize_query(
                child_namespace_identifier
            )
        )
    child_consumer_identifiers = el.find("ConsumerIdentifiers")
    if child_consumer_identifiers is not None:
        import aws_sdk_redshift.types.consumer_identifier_list

        out["consumer_identifiers"] = (
            aws_sdk_redshift.types.consumer_identifier_list.deserialize_query(
                child_consumer_identifiers
            )
        )
    return out
