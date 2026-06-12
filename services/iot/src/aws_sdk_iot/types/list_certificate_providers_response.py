"""Generated from Smithy shape ``com.amazonaws.iot#ListCertificateProvidersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_providers
    import aws_sdk_iot.types.marker


class ListCertificateProvidersResponse(TypedDict):
    certificate_providers: NotRequired[
        "aws_sdk_iot.types.certificate_providers.CertificateProviders"
    ]
    """<p>The list of certificate providers in your Amazon Web Services account.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>The token for the next set of results, or <code>null</code> if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCertificateProvidersResponse) -> dict:
    out: dict = {}
    if "certificate_providers" in value:
        import aws_sdk_iot.types.certificate_providers

        out["certificateProviders"] = (
            aws_sdk_iot.types.certificate_providers.serialize_json(
                value["certificate_providers"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCertificateProvidersResponse:
    out: ListCertificateProvidersResponse = {}  # type: ignore[typeddict-item]
    if "certificateProviders" in data:
        import aws_sdk_iot.types.certificate_providers

        out["certificate_providers"] = (
            aws_sdk_iot.types.certificate_providers.deserialize_json(
                data["certificateProviders"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
