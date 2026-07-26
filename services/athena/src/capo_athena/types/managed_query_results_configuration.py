"""Generated from Smithy shape ``com.amazonaws.athena#ManagedQueryResultsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.boolean
    import capo_athena.types.managed_query_results_encryption_configuration


class ManagedQueryResultsConfiguration(TypedDict, closed=True):
    enabled: "capo_athena.types.boolean.Boolean"
    """<p>If set to true, allows you to store query results in Athena owned storage. If set to false, workgroup member stores query results in location specified under <code>ResultConfiguration$OutputLocation</code>. The default is false. A workgroup cannot have the <code>ResultConfiguration$OutputLocation</code> parameter when you set this field to true. </p>"""
    encryption_configuration: NotRequired[
        "capo_athena.types.managed_query_results_encryption_configuration.ManagedQueryResultsEncryptionConfiguration"
    ]
    """<p>If you encrypt query and calculation results in Athena owned storage, this field indicates the encryption option (for example, SSE_KMS or CSE_KMS) and key information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedQueryResultsConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    if "encryption_configuration" in value:
        import capo_athena.types.managed_query_results_encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_athena.types.managed_query_results_encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedQueryResultsConfiguration:
    out: ManagedQueryResultsConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if "EncryptionConfiguration" in data:
        import capo_athena.types.managed_query_results_encryption_configuration

        out["encryption_configuration"] = (
            capo_athena.types.managed_query_results_encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    return out
