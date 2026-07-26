"""Generated from Smithy shape ``com.amazonaws.sagemaker#IdentityProviderOAuthSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.data_source_name
    import capo_sagemaker.types.feature_status
    import capo_sagemaker.types.secret_arn


class IdentityProviderOAuthSetting(TypedDict, closed=True):
    data_source_name: NotRequired[
        "capo_sagemaker.types.data_source_name.DataSourceName"
    ]
    """<p>The name of the data source that you're connecting to. Canvas currently supports OAuth for Snowflake and Salesforce Data Cloud.</p>"""
    status: NotRequired["capo_sagemaker.types.feature_status.FeatureStatus"]
    """<p>Describes whether OAuth for a data source is enabled or disabled in the Canvas application.</p>"""
    secret_arn: NotRequired["capo_sagemaker.types.secret_arn.SecretArn"]
    """<p>The ARN of an Amazon Web Services Secrets Manager secret that stores the credentials from your identity provider, such as the client ID and secret, authorization URL, and token URL. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityProviderOAuthSetting) -> dict:
    out: dict = {}
    if "data_source_name" in value:
        import capo_sagemaker.types.data_source_name

        out["DataSourceName"] = (
            capo_sagemaker.types.data_source_name.serialize_aws_json_1_1(
                value["data_source_name"]
            )
        )
    if "status" in value:
        import capo_sagemaker.types.feature_status

        out["Status"] = capo_sagemaker.types.feature_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityProviderOAuthSetting:
    out: IdentityProviderOAuthSetting = {}  # type: ignore[typeddict-item]
    if "DataSourceName" in data:
        import capo_sagemaker.types.data_source_name

        out["data_source_name"] = (
            capo_sagemaker.types.data_source_name.deserialize_aws_json_1_1(
                data["DataSourceName"]
            )
        )
    if "Status" in data:
        import capo_sagemaker.types.feature_status

        out["status"] = capo_sagemaker.types.feature_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    return out
