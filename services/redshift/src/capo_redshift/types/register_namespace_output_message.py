"""Generated from Smithy shape ``com.amazonaws.redshift#RegisterNamespaceOutputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.namespace_registration_status


class RegisterNamespaceOutputMessage(TypedDict, closed=True):
    status: NotRequired[
        "capo_redshift.types.namespace_registration_status.NamespaceRegistrationStatus"
    ]
    """<p>The registration status of the cluster or serverless namespace.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RegisterNamespaceOutputMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        import capo_redshift.types.namespace_registration_status

        capo_redshift.types.namespace_registration_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )


def deserialize_query(el: Element) -> RegisterNamespaceOutputMessage:
    out: RegisterNamespaceOutputMessage = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_redshift.types.namespace_registration_status

        out["status"] = (
            capo_redshift.types.namespace_registration_status.deserialize_query(
                child_status
            )
        )
    return out
