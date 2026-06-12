"""Generated from Smithy shape ``com.amazonaws.rds#DeleteIntegrationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.integration_identifier


class DeleteIntegrationMessage(TypedDict):
    integration_identifier: NotRequired[
        "aws_sdk_rds.types.integration_identifier.IntegrationIdentifier"
    ]
    """<p>The unique identifier of the integration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteIntegrationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "integration_identifier" in value:
        pairs.append(
            (f"{prefix}.IntegrationIdentifier", str(value["integration_identifier"]))
        )


def deserialize_query(el: Element) -> DeleteIntegrationMessage:
    out: DeleteIntegrationMessage = {}  # type: ignore[typeddict-item]
    child_integration_identifier = el.find("IntegrationIdentifier")
    if child_integration_identifier is not None:
        out["integration_identifier"] = str(child_integration_identifier.text or "")
    return out
