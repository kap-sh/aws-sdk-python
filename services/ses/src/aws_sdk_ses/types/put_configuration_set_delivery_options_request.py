"""Generated from Smithy shape ``com.amazonaws.ses#PutConfigurationSetDeliveryOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.configuration_set_name
    import aws_sdk_ses.types.delivery_options


class PutConfigurationSetDeliveryOptionsRequest(TypedDict):
    configuration_set_name: (
        "aws_sdk_ses.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set.</p>"""
    delivery_options: NotRequired["aws_sdk_ses.types.delivery_options.DeliveryOptions"]
    """<p>Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PutConfigurationSetDeliveryOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append(
        (f"{prefix}.ConfigurationSetName", str(value["configuration_set_name"]))
    )
    if "delivery_options" in value:
        import aws_sdk_ses.types.delivery_options

        aws_sdk_ses.types.delivery_options.serialize_query(
            value["delivery_options"], pairs, f"{prefix}.DeliveryOptions"
        )


def deserialize_query(el: Element) -> PutConfigurationSetDeliveryOptionsRequest:
    out: PutConfigurationSetDeliveryOptionsRequest = {}  # type: ignore[typeddict-item]
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    else:
        raise DeserializationError(
            "PutConfigurationSetDeliveryOptionsRequest.configuration_set_name required"
        )
    child_delivery_options = el.find("DeliveryOptions")
    if child_delivery_options is not None:
        import aws_sdk_ses.types.delivery_options

        out["delivery_options"] = aws_sdk_ses.types.delivery_options.deserialize_query(
            child_delivery_options
        )
    return out
