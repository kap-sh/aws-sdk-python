"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteIntegrationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integration_arn


class DeleteIntegrationMessage(TypedDict, closed=True):
    integration_arn: NotRequired["capo_redshift.types.integration_arn.IntegrationArn"]
    """<p>The unique identifier of the integration to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteIntegrationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "integration_arn" in value:
        pairs.append((f"{key_prefix}IntegrationArn", str(value["integration_arn"])))


def deserialize_query(el: Element) -> DeleteIntegrationMessage:
    out: DeleteIntegrationMessage = {}  # type: ignore[typeddict-item]
    child_integration_arn = el.find("IntegrationArn")
    if child_integration_arn is not None:
        out["integration_arn"] = str(child_integration_arn.text or "")
    return out
