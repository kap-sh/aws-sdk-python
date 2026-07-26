"""Generated from Smithy shape ``com.amazonaws.glue#AmazonRedshiftNodeData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.amazon_redshift_advanced_options
    import capo_glue.types.boolean_value
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.generic_limited_string
    import capo_glue.types.generic_string
    import capo_glue.types.option
    import capo_glue.types.option_list


class AmazonRedshiftNodeData(TypedDict, closed=True):
    access_type: NotRequired[
        "capo_glue.types.generic_limited_string.GenericLimitedString"
    ]
    """<p>The access type for the Redshift connection. Can be a direct connection or catalog connections.</p>"""
    source_type: NotRequired[
        "capo_glue.types.generic_limited_string.GenericLimitedString"
    ]
    """<p>The source type to specify whether a specific table is the source or a custom query.</p>"""
    connection: NotRequired["capo_glue.types.option.Option"]
    """<p>The Glue connection to the Redshift cluster.</p>"""
    schema: NotRequired["capo_glue.types.option.Option"]
    """<p>The Redshift schema name when working with a direct connection.</p>"""
    table: NotRequired["capo_glue.types.option.Option"]
    """<p>The Redshift table name when working with a direct connection.</p>"""
    catalog_database: NotRequired["capo_glue.types.option.Option"]
    """<p>The name of the Glue Data Catalog database when working with a data catalog.</p>"""
    catalog_table: NotRequired["capo_glue.types.option.Option"]
    """<p>The Glue Data Catalog table name when working with a data catalog.</p>"""
    catalog_redshift_schema: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The Redshift schema name when working with a data catalog.</p>"""
    catalog_redshift_table: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The database table to read from.</p>"""
    temp_dir: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The Amazon S3 path where temporary data can be staged when copying out of the database.</p>"""
    iam_role: NotRequired["capo_glue.types.option.Option"]
    """<p>Optional. The role name use when connection to S3. The IAM role ill default to the role on the job when left blank.</p>"""
    advanced_options: NotRequired[
        "capo_glue.types.amazon_redshift_advanced_options.AmazonRedshiftAdvancedOptions"
    ]
    """<p>Optional values when connecting to the Redshift cluster.</p>"""
    sample_query: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The SQL used to fetch the data from a Redshift sources when the SourceType is 'query'.</p>"""
    pre_action: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The SQL used before a MERGE or APPEND with upsert is run.</p>"""
    post_action: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The SQL used before a MERGE or APPEND with upsert is run.</p>"""
    action: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>Specifies how writing to a Redshift cluser will occur.</p>"""
    table_prefix: NotRequired[
        "capo_glue.types.generic_limited_string.GenericLimitedString"
    ]
    """<p>Specifies the prefix to a table.</p>"""
    upsert: "capo_glue.types.boolean_value.BooleanValue"
    """<p>The action used on Redshift sinks when doing an APPEND.</p>"""
    merge_action: NotRequired[
        "capo_glue.types.generic_limited_string.GenericLimitedString"
    ]
    """<p>The action used when to detemine how a MERGE in a Redshift sink will be handled.</p>"""
    merge_when_matched: NotRequired[
        "capo_glue.types.generic_limited_string.GenericLimitedString"
    ]
    """<p>The action used when to detemine how a MERGE in a Redshift sink will be handled when an existing record matches a new record.</p>"""
    merge_when_not_matched: NotRequired[
        "capo_glue.types.generic_limited_string.GenericLimitedString"
    ]
    """<p>The action used when to detemine how a MERGE in a Redshift sink will be handled when an existing record doesn't match a new record.</p>"""
    merge_clause: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The SQL used in a custom merge to deal with matching records.</p>"""
    crawler_connection: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>Specifies the name of the connection that is associated with the catalog table used.</p>"""
    table_schema: NotRequired["capo_glue.types.option_list.OptionList"]
    """<p>The array of schema output for a given node.</p>"""
    staging_table: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The name of the temporary staging table that is used when doing a MERGE or APPEND with upsert.</p>"""
    selected_columns: NotRequired["capo_glue.types.option_list.OptionList"]
    """<p>The list of column names used to determine a matching record when doing a MERGE or APPEND with upsert.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmazonRedshiftNodeData) -> dict:
    out: dict = {}
    if "access_type" in value:
        out["AccessType"] = value["access_type"]
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    if "connection" in value:
        import capo_glue.types.option

        out["Connection"] = capo_glue.types.option.serialize_aws_json_1_1(
            value["connection"]
        )
    if "schema" in value:
        import capo_glue.types.option

        out["Schema"] = capo_glue.types.option.serialize_aws_json_1_1(value["schema"])
    if "table" in value:
        import capo_glue.types.option

        out["Table"] = capo_glue.types.option.serialize_aws_json_1_1(value["table"])
    if "catalog_database" in value:
        import capo_glue.types.option

        out["CatalogDatabase"] = capo_glue.types.option.serialize_aws_json_1_1(
            value["catalog_database"]
        )
    if "catalog_table" in value:
        import capo_glue.types.option

        out["CatalogTable"] = capo_glue.types.option.serialize_aws_json_1_1(
            value["catalog_table"]
        )
    if "catalog_redshift_schema" in value:
        out["CatalogRedshiftSchema"] = value["catalog_redshift_schema"]
    if "catalog_redshift_table" in value:
        out["CatalogRedshiftTable"] = value["catalog_redshift_table"]
    if "temp_dir" in value:
        out["TempDir"] = value["temp_dir"]
    if "iam_role" in value:
        import capo_glue.types.option

        out["IamRole"] = capo_glue.types.option.serialize_aws_json_1_1(
            value["iam_role"]
        )
    if "advanced_options" in value:
        import capo_glue.types.amazon_redshift_advanced_options

        out["AdvancedOptions"] = (
            capo_glue.types.amazon_redshift_advanced_options.serialize_aws_json_1_1(
                value["advanced_options"]
            )
        )
    if "sample_query" in value:
        out["SampleQuery"] = value["sample_query"]
    if "pre_action" in value:
        out["PreAction"] = value["pre_action"]
    if "post_action" in value:
        out["PostAction"] = value["post_action"]
    if "action" in value:
        out["Action"] = value["action"]
    if "table_prefix" in value:
        out["TablePrefix"] = value["table_prefix"]
    out["Upsert"] = value.get("upsert", False)
    if "merge_action" in value:
        out["MergeAction"] = value["merge_action"]
    if "merge_when_matched" in value:
        out["MergeWhenMatched"] = value["merge_when_matched"]
    if "merge_when_not_matched" in value:
        out["MergeWhenNotMatched"] = value["merge_when_not_matched"]
    if "merge_clause" in value:
        out["MergeClause"] = value["merge_clause"]
    if "crawler_connection" in value:
        out["CrawlerConnection"] = value["crawler_connection"]
    if "table_schema" in value:
        import capo_glue.types.option_list

        out["TableSchema"] = capo_glue.types.option_list.serialize_aws_json_1_1(
            value["table_schema"]
        )
    if "staging_table" in value:
        out["StagingTable"] = value["staging_table"]
    if "selected_columns" in value:
        import capo_glue.types.option_list

        out["SelectedColumns"] = capo_glue.types.option_list.serialize_aws_json_1_1(
            value["selected_columns"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AmazonRedshiftNodeData:
    out: AmazonRedshiftNodeData = {}  # type: ignore[typeddict-item]
    if "AccessType" in data:
        out["access_type"] = data["AccessType"]
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    if "Connection" in data:
        import capo_glue.types.option

        out["connection"] = capo_glue.types.option.deserialize_aws_json_1_1(
            data["Connection"]
        )
    if "Schema" in data:
        import capo_glue.types.option

        out["schema"] = capo_glue.types.option.deserialize_aws_json_1_1(data["Schema"])
    if "Table" in data:
        import capo_glue.types.option

        out["table"] = capo_glue.types.option.deserialize_aws_json_1_1(data["Table"])
    if "CatalogDatabase" in data:
        import capo_glue.types.option

        out["catalog_database"] = capo_glue.types.option.deserialize_aws_json_1_1(
            data["CatalogDatabase"]
        )
    if "CatalogTable" in data:
        import capo_glue.types.option

        out["catalog_table"] = capo_glue.types.option.deserialize_aws_json_1_1(
            data["CatalogTable"]
        )
    if "CatalogRedshiftSchema" in data:
        out["catalog_redshift_schema"] = data["CatalogRedshiftSchema"]
    if "CatalogRedshiftTable" in data:
        out["catalog_redshift_table"] = data["CatalogRedshiftTable"]
    if "TempDir" in data:
        out["temp_dir"] = data["TempDir"]
    if "IamRole" in data:
        import capo_glue.types.option

        out["iam_role"] = capo_glue.types.option.deserialize_aws_json_1_1(
            data["IamRole"]
        )
    if "AdvancedOptions" in data:
        import capo_glue.types.amazon_redshift_advanced_options

        out["advanced_options"] = (
            capo_glue.types.amazon_redshift_advanced_options.deserialize_aws_json_1_1(
                data["AdvancedOptions"]
            )
        )
    if "SampleQuery" in data:
        out["sample_query"] = data["SampleQuery"]
    if "PreAction" in data:
        out["pre_action"] = data["PreAction"]
    if "PostAction" in data:
        out["post_action"] = data["PostAction"]
    if "Action" in data:
        out["action"] = data["Action"]
    if "TablePrefix" in data:
        out["table_prefix"] = data["TablePrefix"]
    if "Upsert" in data:
        out["upsert"] = data["Upsert"]
    else:
        out["upsert"] = False
    if "MergeAction" in data:
        out["merge_action"] = data["MergeAction"]
    if "MergeWhenMatched" in data:
        out["merge_when_matched"] = data["MergeWhenMatched"]
    if "MergeWhenNotMatched" in data:
        out["merge_when_not_matched"] = data["MergeWhenNotMatched"]
    if "MergeClause" in data:
        out["merge_clause"] = data["MergeClause"]
    if "CrawlerConnection" in data:
        out["crawler_connection"] = data["CrawlerConnection"]
    if "TableSchema" in data:
        import capo_glue.types.option_list

        out["table_schema"] = capo_glue.types.option_list.deserialize_aws_json_1_1(
            data["TableSchema"]
        )
    if "StagingTable" in data:
        out["staging_table"] = data["StagingTable"]
    if "SelectedColumns" in data:
        import capo_glue.types.option_list

        out["selected_columns"] = capo_glue.types.option_list.deserialize_aws_json_1_1(
            data["SelectedColumns"]
        )
    return out
