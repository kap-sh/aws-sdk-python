"""Generated from Smithy shape ``com.amazonaws.opensearch#CancelServiceSoftwareUpdateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.service_software_options


class CancelServiceSoftwareUpdateResponse(TypedDict, closed=True):
    service_software_options: NotRequired[
        "aws_sdk_opensearch.types.service_software_options.ServiceSoftwareOptions"
    ]
    """<p>Container for the state of your domain relative to the latest service software.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelServiceSoftwareUpdateResponse) -> dict:
    out: dict = {}
    if "service_software_options" in value:
        import aws_sdk_opensearch.types.service_software_options

        out["ServiceSoftwareOptions"] = (
            aws_sdk_opensearch.types.service_software_options.serialize_json(
                value["service_software_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> CancelServiceSoftwareUpdateResponse:
    out: CancelServiceSoftwareUpdateResponse = {}  # type: ignore[typeddict-item]
    if "ServiceSoftwareOptions" in data:
        import aws_sdk_opensearch.types.service_software_options

        out["service_software_options"] = (
            aws_sdk_opensearch.types.service_software_options.deserialize_json(
                data["ServiceSoftwareOptions"]
            )
        )
    return out
