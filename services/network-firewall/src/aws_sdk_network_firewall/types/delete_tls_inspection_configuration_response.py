"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteTLSInspectionConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.tls_inspection_configuration_response


class DeleteTLSInspectionConfigurationResponse(TypedDict):
    tls_inspection_configuration_response: "aws_sdk_network_firewall.types.tls_inspection_configuration_response.TLSInspectionConfigurationResponse"
    """<p>The high-level properties of a TLS inspection configuration. This, along with the <a>TLSInspectionConfiguration</a>, define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling <a>DescribeTLSInspectionConfiguration</a>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteTLSInspectionConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_network_firewall.types.tls_inspection_configuration_response

    out["TLSInspectionConfigurationResponse"] = (
        aws_sdk_network_firewall.types.tls_inspection_configuration_response.serialize_aws_json_1_0(
            value["tls_inspection_configuration_response"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteTLSInspectionConfigurationResponse:
    out: DeleteTLSInspectionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "TLSInspectionConfigurationResponse" in data:
        import aws_sdk_network_firewall.types.tls_inspection_configuration_response

        out["tls_inspection_configuration_response"] = (
            aws_sdk_network_firewall.types.tls_inspection_configuration_response.deserialize_aws_json_1_0(
                data["TLSInspectionConfigurationResponse"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteTLSInspectionConfigurationResponse.tls_inspection_configuration_response required"
        )
    return out
