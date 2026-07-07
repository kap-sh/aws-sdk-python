"""Generated from Smithy shape ``com.amazonaws.ses#UpdateConfigurationSetEventDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.configuration_set_name
    import aws_sdk_ses.types.event_destination


class UpdateConfigurationSetEventDestinationRequest(TypedDict, closed=True):
    configuration_set_name: (
        "aws_sdk_ses.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set that contains the event destination.</p>"""
    event_destination: "aws_sdk_ses.types.event_destination.EventDestination"
    """<p>The event destination object.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateConfigurationSetEventDestinationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append(
        (f"{prefix}.ConfigurationSetName", str(value["configuration_set_name"]))
    )
    import aws_sdk_ses.types.event_destination

    aws_sdk_ses.types.event_destination.serialize_query(
        value["event_destination"], pairs, f"{prefix}.EventDestination"
    )


def deserialize_query(el: Element) -> UpdateConfigurationSetEventDestinationRequest:
    out: UpdateConfigurationSetEventDestinationRequest = {}  # type: ignore[typeddict-item]
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    else:
        raise DeserializationError(
            "UpdateConfigurationSetEventDestinationRequest.configuration_set_name required"
        )
    child_event_destination = el.find("EventDestination")
    if child_event_destination is not None:
        import aws_sdk_ses.types.event_destination

        out["event_destination"] = (
            aws_sdk_ses.types.event_destination.deserialize_query(
                child_event_destination
            )
        )
    else:
        raise DeserializationError(
            "UpdateConfigurationSetEventDestinationRequest.event_destination required"
        )
    return out
