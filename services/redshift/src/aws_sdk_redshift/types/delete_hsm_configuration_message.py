"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteHsmConfigurationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class DeleteHsmConfigurationMessage(TypedDict, closed=True):
    hsm_configuration_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of the Amazon Redshift HSM configuration to be deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteHsmConfigurationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "hsm_configuration_identifier" in value:
        pairs.append(
            (
                f"{prefix}.HsmConfigurationIdentifier",
                str(value["hsm_configuration_identifier"]),
            )
        )


def deserialize_query(el: Element) -> DeleteHsmConfigurationMessage:
    out: DeleteHsmConfigurationMessage = {}  # type: ignore[typeddict-item]
    child_hsm_configuration_identifier = el.find("HsmConfigurationIdentifier")
    if child_hsm_configuration_identifier is not None:
        out["hsm_configuration_identifier"] = str(
            child_hsm_configuration_identifier.text or ""
        )
    return out
