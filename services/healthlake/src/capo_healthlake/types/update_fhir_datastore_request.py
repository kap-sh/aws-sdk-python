"""Generated from Smithy shape ``com.amazonaws.healthlake#UpdateFHIRDatastoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.analytics_configuration
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.datastore_name
    import capo_healthlake.types.identity_provider_configuration
    import capo_healthlake.types.nlp_configuration
    import capo_healthlake.types.profile_configuration


class UpdateFHIRDatastoreRequest(TypedDict, closed=True):
    datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """<para>The data store identifier.</para>"""
    datastore_name: NotRequired["capo_healthlake.types.datastore_name.DatastoreName"]
    """<para>The data store name.</para>"""
    analytics_configuration: NotRequired[
        "capo_healthlake.types.analytics_configuration.AnalyticsConfiguration"
    ]
    """<para>The analytics configuration for the data store.</para>"""
    nlp_configuration: NotRequired[
        "capo_healthlake.types.nlp_configuration.NlpConfiguration"
    ]
    """<para>The NLP configuration for the data store.</para>"""
    profile_configuration: NotRequired[
        "capo_healthlake.types.profile_configuration.ProfileConfiguration"
    ]
    """<para>The profile configuration for the data store.</para>"""
    identity_provider_configuration: NotRequired[
        "capo_healthlake.types.identity_provider_configuration.IdentityProviderConfiguration"
    ]
    """<para>The identity provider configuration for the data store.</para>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateFHIRDatastoreRequest) -> dict:
    out: dict = {}
    out["DatastoreId"] = value["datastore_id"]
    if "datastore_name" in value:
        out["DatastoreName"] = value["datastore_name"]
    if "analytics_configuration" in value:
        import capo_healthlake.types.analytics_configuration

        out["AnalyticsConfiguration"] = (
            capo_healthlake.types.analytics_configuration.serialize_aws_json_1_0(
                value["analytics_configuration"]
            )
        )
    if "nlp_configuration" in value:
        import capo_healthlake.types.nlp_configuration

        out["NlpConfiguration"] = (
            capo_healthlake.types.nlp_configuration.serialize_aws_json_1_0(
                value["nlp_configuration"]
            )
        )
    if "profile_configuration" in value:
        import capo_healthlake.types.profile_configuration

        out["ProfileConfiguration"] = (
            capo_healthlake.types.profile_configuration.serialize_aws_json_1_0(
                value["profile_configuration"]
            )
        )
    if "identity_provider_configuration" in value:
        import capo_healthlake.types.identity_provider_configuration

        out["IdentityProviderConfiguration"] = (
            capo_healthlake.types.identity_provider_configuration.serialize_aws_json_1_0(
                value["identity_provider_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateFHIRDatastoreRequest:
    out: UpdateFHIRDatastoreRequest = {}  # type: ignore[typeddict-item]
    if "DatastoreId" in data:
        out["datastore_id"] = data["DatastoreId"]
    else:
        raise DeserializationError("UpdateFHIRDatastoreRequest.datastore_id required")
    if "DatastoreName" in data:
        out["datastore_name"] = data["DatastoreName"]
    if "AnalyticsConfiguration" in data:
        import capo_healthlake.types.analytics_configuration

        out["analytics_configuration"] = (
            capo_healthlake.types.analytics_configuration.deserialize_aws_json_1_0(
                data["AnalyticsConfiguration"]
            )
        )
    if "NlpConfiguration" in data:
        import capo_healthlake.types.nlp_configuration

        out["nlp_configuration"] = (
            capo_healthlake.types.nlp_configuration.deserialize_aws_json_1_0(
                data["NlpConfiguration"]
            )
        )
    if "ProfileConfiguration" in data:
        import capo_healthlake.types.profile_configuration

        out["profile_configuration"] = (
            capo_healthlake.types.profile_configuration.deserialize_aws_json_1_0(
                data["ProfileConfiguration"]
            )
        )
    if "IdentityProviderConfiguration" in data:
        import capo_healthlake.types.identity_provider_configuration

        out["identity_provider_configuration"] = (
            capo_healthlake.types.identity_provider_configuration.deserialize_aws_json_1_0(
                data["IdentityProviderConfiguration"]
            )
        )
    return out
