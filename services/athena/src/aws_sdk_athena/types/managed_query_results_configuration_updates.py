"""Generated from Smithy shape ``com.amazonaws.athena#ManagedQueryResultsConfigurationUpdates``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.boxed_boolean
    import aws_sdk_athena.types.managed_query_results_encryption_configuration


class ManagedQueryResultsConfigurationUpdates(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_athena.types.boxed_boolean.BoxedBoolean"]
    """<p>If set to true, specifies that Athena manages query results in Athena owned storage.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_athena.types.managed_query_results_encryption_configuration.ManagedQueryResultsEncryptionConfiguration"
    ]
    """<p>If you encrypt query and calculation results in Athena owned storage, this field indicates the encryption option (for example, SSE_KMS or CSE_KMS) and key information.</p>"""
    remove_encryption_configuration: NotRequired[
        "aws_sdk_athena.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>If set to true, it removes workgroup from Athena owned storage. The existing query results are cleaned up after 24hrs. You must provide query results in location specified under <code>ResultConfiguration$OutputLocation</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedQueryResultsConfigurationUpdates) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "encryption_configuration" in value:
        import aws_sdk_athena.types.managed_query_results_encryption_configuration

        out["EncryptionConfiguration"] = (
            aws_sdk_athena.types.managed_query_results_encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    if "remove_encryption_configuration" in value:
        out["RemoveEncryptionConfiguration"] = value["remove_encryption_configuration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedQueryResultsConfigurationUpdates:
    out: ManagedQueryResultsConfigurationUpdates = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "EncryptionConfiguration" in data:
        import aws_sdk_athena.types.managed_query_results_encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_athena.types.managed_query_results_encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    if "RemoveEncryptionConfiguration" in data:
        out["remove_encryption_configuration"] = data["RemoveEncryptionConfiguration"]
    return out
