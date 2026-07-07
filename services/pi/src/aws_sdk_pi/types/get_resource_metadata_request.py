"""Generated from Smithy shape ``com.amazonaws.pi#GetResourceMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pi.types.identifier_string
    import aws_sdk_pi.types.service_type


class GetResourceMetadataRequest(TypedDict, closed=True):
    service_type: "aws_sdk_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights returns metrics.</p>"""
    identifier: "aws_sdk_pi.types.identifier_string.IdentifierString"
    """<p>An immutable identifier for a data source that is unique for an Amazon Web Services Region. Performance Insights gathers metrics from this data source. To use a DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VW2X</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourceMetadataRequest) -> dict:
    out: dict = {}
    import aws_sdk_pi.types.service_type

    out["ServiceType"] = aws_sdk_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourceMetadataRequest:
    out: GetResourceMetadataRequest = {}  # type: ignore[typeddict-item]
    if "ServiceType" in data:
        import aws_sdk_pi.types.service_type

        out["service_type"] = aws_sdk_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        raise DeserializationError("GetResourceMetadataRequest.service_type required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("GetResourceMetadataRequest.identifier required")
    return out
