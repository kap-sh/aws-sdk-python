"""Generated from Smithy shape ``com.amazonaws.docdb#DBEngineVersion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.boolean
    import aws_sdk_docdb.types.boolean_optional
    import aws_sdk_docdb.types.ca_certificate_identifiers_list
    import aws_sdk_docdb.types.log_type_list
    import aws_sdk_docdb.types.serverless_v2_features_support
    import aws_sdk_docdb.types.string
    import aws_sdk_docdb.types.valid_upgrade_target_list


class DBEngineVersion(TypedDict):
    engine: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The name of the database engine.</p>"""
    engine_version: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The version number of the database engine.</p>"""
    db_parameter_group_family: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The name of the parameter group family for the database engine.</p>"""
    db_engine_description: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The description of the database engine.</p>"""
    db_engine_version_description: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The description of the database engine version.</p>"""
    valid_upgrade_target: NotRequired[
        "aws_sdk_docdb.types.valid_upgrade_target_list.ValidUpgradeTargetList"
    ]
    """<p>A list of engine versions that this database engine version can be upgraded to.</p>"""
    exportable_log_types: NotRequired["aws_sdk_docdb.types.log_type_list.LogTypeList"]
    """<p>The types of logs that the database engine has available for export to Amazon CloudWatch Logs.</p>"""
    supports_log_exports_to_cloudwatch_logs: NotRequired[
        "aws_sdk_docdb.types.boolean.Boolean"
    ]
    """<p>A value that indicates whether the engine version supports exporting the log types specified by <code>ExportableLogTypes</code> to CloudWatch Logs.</p>"""
    supported_ca_certificate_identifiers: NotRequired[
        "aws_sdk_docdb.types.ca_certificate_identifiers_list.CACertificateIdentifiersList"
    ]
    r"""<p>A list of the supported CA certificate identifiers.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/documentdb/latest/developerguide/ca_cert_rotation.html\">Updating Your Amazon DocumentDB TLS Certificates</a> and <a href=\"https://docs.aws.amazon.com/documentdb/latest/developerguide/security.encryption.ssl.html\"> Encrypting Data in Transit</a> in the <i>Amazon DocumentDB Developer Guide</i>.</p>"""
    supports_certificate_rotation_without_restart: NotRequired[
        "aws_sdk_docdb.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the engine version supports rotating the server certificate without rebooting the DB instance.</p>"""
    serverless_v2_features_support: NotRequired[
        "aws_sdk_docdb.types.serverless_v2_features_support.ServerlessV2FeaturesSupport"
    ]
    """<p>Specifies any Amazon DocumentDB Serverless properties or limits that differ between Amazon DocumentDB engine versions. You can test the values of this attribute when deciding which Amazon DocumentDB version to use in a new or upgraded cluster. You can also retrieve the version of an existing cluster and check whether that version supports certain Amazon DocumentDB Serverless features before you attempt to use those features.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBEngineVersion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{prefix}.EngineVersion", str(value["engine_version"])))
    if "db_parameter_group_family" in value:
        pairs.append(
            (
                f"{prefix}.DBParameterGroupFamily",
                str(value["db_parameter_group_family"]),
            )
        )
    if "db_engine_description" in value:
        pairs.append(
            (f"{prefix}.DBEngineDescription", str(value["db_engine_description"]))
        )
    if "db_engine_version_description" in value:
        pairs.append(
            (
                f"{prefix}.DBEngineVersionDescription",
                str(value["db_engine_version_description"]),
            )
        )
    if "valid_upgrade_target" in value:
        import aws_sdk_docdb.types.valid_upgrade_target_list

        aws_sdk_docdb.types.valid_upgrade_target_list.serialize_query(
            value["valid_upgrade_target"], pairs, f"{prefix}.ValidUpgradeTarget"
        )
    if "exportable_log_types" in value:
        import aws_sdk_docdb.types.log_type_list

        aws_sdk_docdb.types.log_type_list.serialize_query(
            value["exportable_log_types"], pairs, f"{prefix}.ExportableLogTypes"
        )
    if "supports_log_exports_to_cloudwatch_logs" in value:
        pairs.append(
            (
                f"{prefix}.SupportsLogExportsToCloudwatchLogs",
                "true" if value["supports_log_exports_to_cloudwatch_logs"] else "false",
            )
        )
    if "supported_ca_certificate_identifiers" in value:
        import aws_sdk_docdb.types.ca_certificate_identifiers_list

        aws_sdk_docdb.types.ca_certificate_identifiers_list.serialize_query(
            value["supported_ca_certificate_identifiers"],
            pairs,
            f"{prefix}.SupportedCACertificateIdentifiers",
        )
    if "supports_certificate_rotation_without_restart" in value:
        pairs.append(
            (
                f"{prefix}.SupportsCertificateRotationWithoutRestart",
                "true"
                if value["supports_certificate_rotation_without_restart"]
                else "false",
            )
        )
    if "serverless_v2_features_support" in value:
        import aws_sdk_docdb.types.serverless_v2_features_support

        aws_sdk_docdb.types.serverless_v2_features_support.serialize_query(
            value["serverless_v2_features_support"],
            pairs,
            f"{prefix}.ServerlessV2FeaturesSupport",
        )


def deserialize_query(el: Element) -> DBEngineVersion:
    out: DBEngineVersion = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_db_parameter_group_family = el.find("DBParameterGroupFamily")
    if child_db_parameter_group_family is not None:
        out["db_parameter_group_family"] = str(
            child_db_parameter_group_family.text or ""
        )
    child_db_engine_description = el.find("DBEngineDescription")
    if child_db_engine_description is not None:
        out["db_engine_description"] = str(child_db_engine_description.text or "")
    child_db_engine_version_description = el.find("DBEngineVersionDescription")
    if child_db_engine_version_description is not None:
        out["db_engine_version_description"] = str(
            child_db_engine_version_description.text or ""
        )
    child_valid_upgrade_target = el.find("ValidUpgradeTarget")
    if child_valid_upgrade_target is not None:
        import aws_sdk_docdb.types.valid_upgrade_target_list

        out["valid_upgrade_target"] = (
            aws_sdk_docdb.types.valid_upgrade_target_list.deserialize_query(
                child_valid_upgrade_target
            )
        )
    child_exportable_log_types = el.find("ExportableLogTypes")
    if child_exportable_log_types is not None:
        import aws_sdk_docdb.types.log_type_list

        out["exportable_log_types"] = (
            aws_sdk_docdb.types.log_type_list.deserialize_query(
                child_exportable_log_types
            )
        )
    child_supports_log_exports_to_cloudwatch_logs = el.find(
        "SupportsLogExportsToCloudwatchLogs"
    )
    if child_supports_log_exports_to_cloudwatch_logs is not None:
        out["supports_log_exports_to_cloudwatch_logs"] = (
            child_supports_log_exports_to_cloudwatch_logs.text or ""
        ).lower() == "true"
    child_supported_ca_certificate_identifiers = el.find(
        "SupportedCACertificateIdentifiers"
    )
    if child_supported_ca_certificate_identifiers is not None:
        import aws_sdk_docdb.types.ca_certificate_identifiers_list

        out["supported_ca_certificate_identifiers"] = (
            aws_sdk_docdb.types.ca_certificate_identifiers_list.deserialize_query(
                child_supported_ca_certificate_identifiers
            )
        )
    child_supports_certificate_rotation_without_restart = el.find(
        "SupportsCertificateRotationWithoutRestart"
    )
    if child_supports_certificate_rotation_without_restart is not None:
        out["supports_certificate_rotation_without_restart"] = (
            child_supports_certificate_rotation_without_restart.text or ""
        ).lower() == "true"
    child_serverless_v2_features_support = el.find("ServerlessV2FeaturesSupport")
    if child_serverless_v2_features_support is not None:
        import aws_sdk_docdb.types.serverless_v2_features_support

        out["serverless_v2_features_support"] = (
            aws_sdk_docdb.types.serverless_v2_features_support.deserialize_query(
                child_serverless_v2_features_support
            )
        )
    return out
