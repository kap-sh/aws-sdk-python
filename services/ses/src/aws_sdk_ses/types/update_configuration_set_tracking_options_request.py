"""Generated from Smithy shape ``com.amazonaws.ses#UpdateConfigurationSetTrackingOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.configuration_set_name
    import aws_sdk_ses.types.tracking_options


class UpdateConfigurationSetTrackingOptionsRequest(TypedDict):
    configuration_set_name: (
        "aws_sdk_ses.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set.</p>"""
    tracking_options: "aws_sdk_ses.types.tracking_options.TrackingOptions"


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateConfigurationSetTrackingOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append(
        (f"{prefix}.ConfigurationSetName", str(value["configuration_set_name"]))
    )
    import aws_sdk_ses.types.tracking_options

    aws_sdk_ses.types.tracking_options.serialize_query(
        value["tracking_options"], pairs, f"{prefix}.TrackingOptions"
    )


def deserialize_query(el: Element) -> UpdateConfigurationSetTrackingOptionsRequest:
    out: UpdateConfigurationSetTrackingOptionsRequest = {}  # type: ignore[typeddict-item]
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    else:
        raise DeserializationError(
            "UpdateConfigurationSetTrackingOptionsRequest.configuration_set_name required"
        )
    child_tracking_options = el.find("TrackingOptions")
    if child_tracking_options is not None:
        import aws_sdk_ses.types.tracking_options

        out["tracking_options"] = aws_sdk_ses.types.tracking_options.deserialize_query(
            child_tracking_options
        )
    else:
        raise DeserializationError(
            "UpdateConfigurationSetTrackingOptionsRequest.tracking_options required"
        )
    return out
