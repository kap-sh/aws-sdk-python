"""Generated from Smithy shape ``com.amazonaws.opensearch#StartServiceSoftwareUpdateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.service_software_options


class StartServiceSoftwareUpdateResponse(TypedDict, closed=True):
    service_software_options: NotRequired[
        "aws_sdk_opensearch.types.service_software_options.ServiceSoftwareOptions"
    ]
    """<p>The current status of the OpenSearch Service software update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartServiceSoftwareUpdateResponse) -> dict:
    out: dict = {}
    if "service_software_options" in value:
        import aws_sdk_opensearch.types.service_software_options

        out["ServiceSoftwareOptions"] = (
            aws_sdk_opensearch.types.service_software_options.serialize_json(
                value["service_software_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartServiceSoftwareUpdateResponse:
    out: StartServiceSoftwareUpdateResponse = {}  # type: ignore[typeddict-item]
    if "ServiceSoftwareOptions" in data:
        import aws_sdk_opensearch.types.service_software_options

        out["service_software_options"] = (
            aws_sdk_opensearch.types.service_software_options.deserialize_json(
                data["ServiceSoftwareOptions"]
            )
        )
    return out
