"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#MutualTlsAuthenticationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.string_with_length_between1_and64
    import aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048


class MutualTlsAuthenticationInput(TypedDict):
    truststore_uri: NotRequired[
        "aws_sdk_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
    ]
    """<p>An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example, s3://<replaceable>bucket-name</replaceable>/<replaceable>key-name</replaceable>. The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version. To update the truststore, you must have permissions to access the S3 object.</p>"""
    truststore_version: NotRequired[
        "aws_sdk_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
    ]
    """<p>The version of the S3 object that contains your truststore. To specify a version, you must have versioning enabled for the S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MutualTlsAuthenticationInput) -> dict:
    out: dict = {}
    if "truststore_uri" in value:
        out["truststoreUri"] = value["truststore_uri"]
    if "truststore_version" in value:
        out["truststoreVersion"] = value["truststore_version"]
    return out


def deserialize_json(data: dict) -> MutualTlsAuthenticationInput:
    out: MutualTlsAuthenticationInput = {}  # type: ignore[typeddict-item]
    if "truststoreUri" in data:
        out["truststore_uri"] = data["truststoreUri"]
    if "truststoreVersion" in data:
        out["truststore_version"] = data["truststoreVersion"]
    return out
