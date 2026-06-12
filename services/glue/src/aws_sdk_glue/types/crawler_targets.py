"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerTargets``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_target_list
    import aws_sdk_glue.types.delta_target_list
    import aws_sdk_glue.types.dynamo_db_target_list
    import aws_sdk_glue.types.hudi_target_list
    import aws_sdk_glue.types.iceberg_target_list
    import aws_sdk_glue.types.jdbc_target_list
    import aws_sdk_glue.types.mongo_db_target_list
    import aws_sdk_glue.types.s3_target_list


class CrawlerTargets(TypedDict):
    s3_targets: NotRequired["aws_sdk_glue.types.s3_target_list.S3TargetList"]
    """<p>Specifies Amazon Simple Storage Service (Amazon S3) targets.</p>"""
    jdbc_targets: NotRequired["aws_sdk_glue.types.jdbc_target_list.JdbcTargetList"]
    """<p>Specifies JDBC targets.</p>"""
    mongo_db_targets: NotRequired[
        "aws_sdk_glue.types.mongo_db_target_list.MongoDBTargetList"
    ]
    """<p>Specifies Amazon DocumentDB or MongoDB targets.</p>"""
    dynamo_db_targets: NotRequired[
        "aws_sdk_glue.types.dynamo_db_target_list.DynamoDBTargetList"
    ]
    """<p>Specifies Amazon DynamoDB targets.</p>"""
    catalog_targets: NotRequired[
        "aws_sdk_glue.types.catalog_target_list.CatalogTargetList"
    ]
    """<p>Specifies Glue Data Catalog targets.</p>"""
    delta_targets: NotRequired["aws_sdk_glue.types.delta_target_list.DeltaTargetList"]
    """<p>Specifies Delta data store targets.</p>"""
    iceberg_targets: NotRequired[
        "aws_sdk_glue.types.iceberg_target_list.IcebergTargetList"
    ]
    """<p>Specifies Apache Iceberg data store targets.</p>"""
    hudi_targets: NotRequired["aws_sdk_glue.types.hudi_target_list.HudiTargetList"]
    """<p>Specifies Apache Hudi data store targets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlerTargets) -> dict:
    out: dict = {}
    if "s3_targets" in value:
        import aws_sdk_glue.types.s3_target_list

        out["S3Targets"] = aws_sdk_glue.types.s3_target_list.serialize_aws_json_1_1(
            value["s3_targets"]
        )
    if "jdbc_targets" in value:
        import aws_sdk_glue.types.jdbc_target_list

        out["JdbcTargets"] = aws_sdk_glue.types.jdbc_target_list.serialize_aws_json_1_1(
            value["jdbc_targets"]
        )
    if "mongo_db_targets" in value:
        import aws_sdk_glue.types.mongo_db_target_list

        out["MongoDBTargets"] = (
            aws_sdk_glue.types.mongo_db_target_list.serialize_aws_json_1_1(
                value["mongo_db_targets"]
            )
        )
    if "dynamo_db_targets" in value:
        import aws_sdk_glue.types.dynamo_db_target_list

        out["DynamoDBTargets"] = (
            aws_sdk_glue.types.dynamo_db_target_list.serialize_aws_json_1_1(
                value["dynamo_db_targets"]
            )
        )
    if "catalog_targets" in value:
        import aws_sdk_glue.types.catalog_target_list

        out["CatalogTargets"] = (
            aws_sdk_glue.types.catalog_target_list.serialize_aws_json_1_1(
                value["catalog_targets"]
            )
        )
    if "delta_targets" in value:
        import aws_sdk_glue.types.delta_target_list

        out["DeltaTargets"] = (
            aws_sdk_glue.types.delta_target_list.serialize_aws_json_1_1(
                value["delta_targets"]
            )
        )
    if "iceberg_targets" in value:
        import aws_sdk_glue.types.iceberg_target_list

        out["IcebergTargets"] = (
            aws_sdk_glue.types.iceberg_target_list.serialize_aws_json_1_1(
                value["iceberg_targets"]
            )
        )
    if "hudi_targets" in value:
        import aws_sdk_glue.types.hudi_target_list

        out["HudiTargets"] = aws_sdk_glue.types.hudi_target_list.serialize_aws_json_1_1(
            value["hudi_targets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CrawlerTargets:
    out: CrawlerTargets = {}  # type: ignore[typeddict-item]
    if "S3Targets" in data:
        import aws_sdk_glue.types.s3_target_list

        out["s3_targets"] = aws_sdk_glue.types.s3_target_list.deserialize_aws_json_1_1(
            data["S3Targets"]
        )
    if "JdbcTargets" in data:
        import aws_sdk_glue.types.jdbc_target_list

        out["jdbc_targets"] = (
            aws_sdk_glue.types.jdbc_target_list.deserialize_aws_json_1_1(
                data["JdbcTargets"]
            )
        )
    if "MongoDBTargets" in data:
        import aws_sdk_glue.types.mongo_db_target_list

        out["mongo_db_targets"] = (
            aws_sdk_glue.types.mongo_db_target_list.deserialize_aws_json_1_1(
                data["MongoDBTargets"]
            )
        )
    if "DynamoDBTargets" in data:
        import aws_sdk_glue.types.dynamo_db_target_list

        out["dynamo_db_targets"] = (
            aws_sdk_glue.types.dynamo_db_target_list.deserialize_aws_json_1_1(
                data["DynamoDBTargets"]
            )
        )
    if "CatalogTargets" in data:
        import aws_sdk_glue.types.catalog_target_list

        out["catalog_targets"] = (
            aws_sdk_glue.types.catalog_target_list.deserialize_aws_json_1_1(
                data["CatalogTargets"]
            )
        )
    if "DeltaTargets" in data:
        import aws_sdk_glue.types.delta_target_list

        out["delta_targets"] = (
            aws_sdk_glue.types.delta_target_list.deserialize_aws_json_1_1(
                data["DeltaTargets"]
            )
        )
    if "IcebergTargets" in data:
        import aws_sdk_glue.types.iceberg_target_list

        out["iceberg_targets"] = (
            aws_sdk_glue.types.iceberg_target_list.deserialize_aws_json_1_1(
                data["IcebergTargets"]
            )
        )
    if "HudiTargets" in data:
        import aws_sdk_glue.types.hudi_target_list

        out["hudi_targets"] = (
            aws_sdk_glue.types.hudi_target_list.deserialize_aws_json_1_1(
                data["HudiTargets"]
            )
        )
    return out
