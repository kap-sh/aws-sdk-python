"""Generated from Smithy shape ``com.amazonaws.ses#DeleteConfigurationSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.configuration_set_name


class DeleteConfigurationSetRequest(TypedDict, closed=True):
    configuration_set_name: "capo_ses.types.configuration_set_name.ConfigurationSetName"
    """<p>The name of the configuration set to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteConfigurationSetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append(
        (f"{prefix}.ConfigurationSetName", str(value["configuration_set_name"]))
    )


def deserialize_query(el: Element) -> DeleteConfigurationSetRequest:
    out: DeleteConfigurationSetRequest = {}  # type: ignore[typeddict-item]
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    else:
        raise DeserializationError(
            "DeleteConfigurationSetRequest.configuration_set_name required"
        )
    return out
