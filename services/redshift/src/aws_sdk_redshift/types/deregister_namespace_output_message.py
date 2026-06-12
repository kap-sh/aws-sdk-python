"""Generated from Smithy shape ``com.amazonaws.redshift#DeregisterNamespaceOutputMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.namespace_registration_status


class DeregisterNamespaceOutputMessage(TypedDict):
    status: NotRequired[
        "aws_sdk_redshift.types.namespace_registration_status.NamespaceRegistrationStatus"
    ]
    """<p>The registration status of the cluster or serverless namespace.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeregisterNamespaceOutputMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "status" in value:
        import aws_sdk_redshift.types.namespace_registration_status

        aws_sdk_redshift.types.namespace_registration_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_query(el: Element) -> DeregisterNamespaceOutputMessage:
    out: DeregisterNamespaceOutputMessage = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_redshift.types.namespace_registration_status

        out["status"] = (
            aws_sdk_redshift.types.namespace_registration_status.deserialize_query(
                child_status
            )
        )
    return out
