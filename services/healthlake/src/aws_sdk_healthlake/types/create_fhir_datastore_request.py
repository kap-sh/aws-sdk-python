"""Generated from Smithy shape ``com.amazonaws.healthlake#CreateFHIRDatastoreRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.client_token_string
    import aws_sdk_healthlake.types.datastore_name
    import aws_sdk_healthlake.types.fhir_version
    import aws_sdk_healthlake.types.identity_provider_configuration
    import aws_sdk_healthlake.types.preload_data_config
    import aws_sdk_healthlake.types.sse_configuration
    import aws_sdk_healthlake.types.tag_list


class CreateFHIRDatastoreRequest(TypedDict):
    datastore_name: NotRequired["aws_sdk_healthlake.types.datastore_name.DatastoreName"]
    """<p>The data store name (user-generated).</p>"""
    datastore_type_version: "aws_sdk_healthlake.types.fhir_version.FHIRVersion"
    """<p>The FHIR release version supported by the data store. Current support is for version <code>R4</code>.</p>"""
    sse_configuration: NotRequired[
        "aws_sdk_healthlake.types.sse_configuration.SseConfiguration"
    ]
    """<p>The server-side encryption key configuration for a customer-provided encryption key specified for creating a data store. </p>"""
    preload_data_config: NotRequired[
        "aws_sdk_healthlake.types.preload_data_config.PreloadDataConfig"
    ]
    """<p>An optional parameter to preload (import) open source Synthea FHIR data upon creation of the data store.</p>"""
    client_token: NotRequired[
        "aws_sdk_healthlake.types.client_token_string.ClientTokenString"
    ]
    """<p>An optional user-provided token to ensure API idempotency.</p>"""
    tags: NotRequired["aws_sdk_healthlake.types.tag_list.TagList"]
    """<p>The resource tags applied to a data store when it is created.</p>"""
    identity_provider_configuration: NotRequired[
        "aws_sdk_healthlake.types.identity_provider_configuration.IdentityProviderConfiguration"
    ]
    """<p>The identity provider configuration to use for the data store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateFHIRDatastoreRequest) -> dict:
    out: dict = {}
    if "datastore_name" in value:
        out["DatastoreName"] = value["datastore_name"]
    import aws_sdk_healthlake.types.fhir_version

    out["DatastoreTypeVersion"] = (
        aws_sdk_healthlake.types.fhir_version.serialize_aws_json_1_0(
            value["datastore_type_version"]
        )
    )
    if "sse_configuration" in value:
        import aws_sdk_healthlake.types.sse_configuration

        out["SseConfiguration"] = (
            aws_sdk_healthlake.types.sse_configuration.serialize_aws_json_1_0(
                value["sse_configuration"]
            )
        )
    if "preload_data_config" in value:
        import aws_sdk_healthlake.types.preload_data_config

        out["PreloadDataConfig"] = (
            aws_sdk_healthlake.types.preload_data_config.serialize_aws_json_1_0(
                value["preload_data_config"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_healthlake.types.tag_list

        out["Tags"] = aws_sdk_healthlake.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "identity_provider_configuration" in value:
        import aws_sdk_healthlake.types.identity_provider_configuration

        out["IdentityProviderConfiguration"] = (
            aws_sdk_healthlake.types.identity_provider_configuration.serialize_aws_json_1_0(
                value["identity_provider_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateFHIRDatastoreRequest:
    out: CreateFHIRDatastoreRequest = {}  # type: ignore[typeddict-item]
    if "DatastoreName" in data:
        out["datastore_name"] = data["DatastoreName"]
    if "DatastoreTypeVersion" in data:
        import aws_sdk_healthlake.types.fhir_version

        out["datastore_type_version"] = (
            aws_sdk_healthlake.types.fhir_version.deserialize_aws_json_1_0(
                data["DatastoreTypeVersion"]
            )
        )
    else:
        raise DeserializationError(
            "CreateFHIRDatastoreRequest.datastore_type_version required"
        )
    if "SseConfiguration" in data:
        import aws_sdk_healthlake.types.sse_configuration

        out["sse_configuration"] = (
            aws_sdk_healthlake.types.sse_configuration.deserialize_aws_json_1_0(
                data["SseConfiguration"]
            )
        )
    if "PreloadDataConfig" in data:
        import aws_sdk_healthlake.types.preload_data_config

        out["preload_data_config"] = (
            aws_sdk_healthlake.types.preload_data_config.deserialize_aws_json_1_0(
                data["PreloadDataConfig"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Tags" in data:
        import aws_sdk_healthlake.types.tag_list

        out["tags"] = aws_sdk_healthlake.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if "IdentityProviderConfiguration" in data:
        import aws_sdk_healthlake.types.identity_provider_configuration

        out["identity_provider_configuration"] = (
            aws_sdk_healthlake.types.identity_provider_configuration.deserialize_aws_json_1_0(
                data["IdentityProviderConfiguration"]
            )
        )
    return out
