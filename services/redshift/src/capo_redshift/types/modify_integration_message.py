"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyIntegrationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integration_arn
    import capo_redshift.types.integration_description
    import capo_redshift.types.integration_name


class ModifyIntegrationMessage(TypedDict, closed=True):
    integration_arn: NotRequired["capo_redshift.types.integration_arn.IntegrationArn"]
    """<p>The unique identifier of the integration to modify.</p>"""
    description: NotRequired[
        "capo_redshift.types.integration_description.IntegrationDescription"
    ]
    """<p>A new description for the integration.</p>"""
    integration_name: NotRequired[
        "capo_redshift.types.integration_name.IntegrationName"
    ]
    """<p>A new name for the integration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyIntegrationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "integration_arn" in value:
        pairs.append((f"{prefix}.IntegrationArn", str(value["integration_arn"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "integration_name" in value:
        pairs.append((f"{prefix}.IntegrationName", str(value["integration_name"])))


def deserialize_query(el: Element) -> ModifyIntegrationMessage:
    out: ModifyIntegrationMessage = {}  # type: ignore[typeddict-item]
    child_integration_arn = el.find("IntegrationArn")
    if child_integration_arn is not None:
        out["integration_arn"] = str(child_integration_arn.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_integration_name = el.find("IntegrationName")
    if child_integration_name is not None:
        out["integration_name"] = str(child_integration_name.text or "")
    return out
