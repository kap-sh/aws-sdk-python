"""Generated from Smithy shape ``com.amazonaws.datazone#GlueRunConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.relational_filter_configurations


class GlueRunConfigurationOutput(TypedDict, closed=True):
    account_id: NotRequired["str"]
    """<p>The Amazon Web Services account ID included in the configuration details of the Amazon Web Services Glue data source. </p>"""
    region: NotRequired["str"]
    """<p>The Amazon Web Services region included in the configuration details of the Amazon Web Services Glue data source. </p>"""
    data_access_role: NotRequired["str"]
    """<p>The data access role included in the configuration details of the Amazon Web Services Glue data source. </p>"""
    relational_filter_configurations: "capo_datazone.types.relational_filter_configurations.RelationalFilterConfigurations"
    """<p>The relational filter configurations included in the configuration details of the Amazon Web Services Glue data source.</p>"""
    auto_import_data_quality_result: NotRequired["bool"]
    """<p>Specifies whether to automatically import data quality metrics as part of the data source run.</p>"""
    catalog_name: NotRequired["str"]
    """<p>The catalog name in the Amazon Web Services Glue run configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlueRunConfigurationOutput) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        out["region"] = value["region"]
    if "data_access_role" in value:
        out["dataAccessRole"] = value["data_access_role"]
    import capo_datazone.types.relational_filter_configurations

    out["relationalFilterConfigurations"] = (
        capo_datazone.types.relational_filter_configurations.serialize_json(
            value["relational_filter_configurations"]
        )
    )
    if "auto_import_data_quality_result" in value:
        out["autoImportDataQualityResult"] = value["auto_import_data_quality_result"]
    if "catalog_name" in value:
        out["catalogName"] = value["catalog_name"]
    return out


def deserialize_json(data: dict) -> GlueRunConfigurationOutput:
    out: GlueRunConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "region" in data:
        out["region"] = data["region"]
    if "dataAccessRole" in data:
        out["data_access_role"] = data["dataAccessRole"]
    if "relationalFilterConfigurations" in data:
        import capo_datazone.types.relational_filter_configurations

        out["relational_filter_configurations"] = (
            capo_datazone.types.relational_filter_configurations.deserialize_json(
                data["relationalFilterConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "GlueRunConfigurationOutput.relational_filter_configurations required"
        )
    if "autoImportDataQualityResult" in data:
        out["auto_import_data_quality_result"] = data["autoImportDataQualityResult"]
    if "catalogName" in data:
        out["catalog_name"] = data["catalogName"]
    return out
