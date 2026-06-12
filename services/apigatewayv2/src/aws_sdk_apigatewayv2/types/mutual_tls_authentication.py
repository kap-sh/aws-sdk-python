"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#MutualTlsAuthentication``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__list_of__string
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and64
    import aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048


class MutualTlsAuthentication(TypedDict):
    truststore_uri: NotRequired[
        "aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
    ]
    """<p>An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example, s3://<replaceable>bucket-name</replaceable>/<replaceable>key-name</replaceable>. The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version. To update the truststore, you must have permissions to access the S3 object.</p>"""
    truststore_version: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
    ]
    """<p>The version of the S3 object that contains your truststore. To specify a version, you must have versioning enabled for the S3 bucket.</p>"""
    truststore_warnings: NotRequired[
        "aws_sdk_apigatewayv2.types.__list_of__string.__listOf__string"
    ]
    """<p>A list of warnings that API Gateway returns while processing your truststore. Invalid certificates produce warnings. Mutual TLS is still enabled, but some clients might not be able to access your API. To resolve warnings, upload a new truststore to S3, and then update you domain name to use the new version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MutualTlsAuthentication) -> dict:
    out: dict = {}
    if "truststore_uri" in value:
        out["truststoreUri"] = value["truststore_uri"]
    if "truststore_version" in value:
        out["truststoreVersion"] = value["truststore_version"]
    if "truststore_warnings" in value:
        import aws_sdk_apigatewayv2.types.__list_of__string

        out["truststoreWarnings"] = (
            aws_sdk_apigatewayv2.types.__list_of__string.serialize_json(
                value["truststore_warnings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MutualTlsAuthentication:
    out: MutualTlsAuthentication = {}  # type: ignore[typeddict-item]
    if "truststoreUri" in data:
        out["truststore_uri"] = data["truststoreUri"]
    if "truststoreVersion" in data:
        out["truststore_version"] = data["truststoreVersion"]
    if "truststoreWarnings" in data:
        import aws_sdk_apigatewayv2.types.__list_of__string

        out["truststore_warnings"] = (
            aws_sdk_apigatewayv2.types.__list_of__string.deserialize_json(
                data["truststoreWarnings"]
            )
        )
    return out
