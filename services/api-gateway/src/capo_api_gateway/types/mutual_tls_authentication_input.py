"""Generated from Smithy shape ``com.amazonaws.apigateway#MutualTlsAuthenticationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.string


class MutualTlsAuthenticationInput(TypedDict, closed=True):
    truststore_uri: NotRequired["capo_api_gateway.types.string.String"]
    """<p>An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example <code>s3://bucket-name/key-name</code>. The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version. To update the truststore, you must have permissions to access the S3 object.</p>"""
    truststore_version: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The version of the S3 object that contains your truststore. To specify a version, you must have versioning enabled for the S3 bucket</p>"""


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
