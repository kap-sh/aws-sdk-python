"""Generated from Smithy shape ``com.amazonaws.sagemaker#QueryFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.query_lineage_types
    import aws_sdk_sagemaker.types.query_properties
    import aws_sdk_sagemaker.types.query_types
    import aws_sdk_sagemaker.types.timestamp


class QueryFilters(TypedDict):
    types: NotRequired["aws_sdk_sagemaker.types.query_types.QueryTypes"]
    """<p>Filter the lineage entities connected to the <code>StartArn</code> by type. For example: <code>DataSet</code>, <code>Model</code>, <code>Endpoint</code>, or <code>ModelDeployment</code>.</p>"""
    lineage_types: NotRequired[
        "aws_sdk_sagemaker.types.query_lineage_types.QueryLineageTypes"
    ]
    """<p>Filter the lineage entities connected to the <code>StartArn</code>(s) by the type of the lineage entity.</p>"""
    created_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Filter the lineage entities connected to the <code>StartArn</code>(s) by created date.</p>"""
    created_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Filter the lineage entities connected to the <code>StartArn</code>(s) after the create date.</p>"""
    modified_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Filter the lineage entities connected to the <code>StartArn</code>(s) before the last modified date.</p>"""
    modified_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Filter the lineage entities connected to the <code>StartArn</code>(s) after the last modified date.</p>"""
    properties: NotRequired["aws_sdk_sagemaker.types.query_properties.QueryProperties"]
    """<p>Filter the lineage entities connected to the <code>StartArn</code>(s) by a set if property key value pairs. If multiple pairs are provided, an entity is included in the results if it matches any of the provided pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryFilters) -> dict:
    out: dict = {}
    if "types" in value:
        import aws_sdk_sagemaker.types.query_types

        out["Types"] = aws_sdk_sagemaker.types.query_types.serialize_aws_json_1_1(
            value["types"]
        )
    if "lineage_types" in value:
        import aws_sdk_sagemaker.types.query_lineage_types

        out["LineageTypes"] = (
            aws_sdk_sagemaker.types.query_lineage_types.serialize_aws_json_1_1(
                value["lineage_types"]
            )
        )
    if "created_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedBefore"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "created_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedAfter"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "modified_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["ModifiedBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["modified_before"]
            )
        )
    if "modified_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["ModifiedAfter"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["modified_after"]
        )
    if "properties" in value:
        import aws_sdk_sagemaker.types.query_properties

        out["Properties"] = (
            aws_sdk_sagemaker.types.query_properties.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryFilters:
    out: QueryFilters = {}  # type: ignore[typeddict-item]
    if "Types" in data:
        import aws_sdk_sagemaker.types.query_types

        out["types"] = aws_sdk_sagemaker.types.query_types.deserialize_aws_json_1_1(
            data["Types"]
        )
    if "LineageTypes" in data:
        import aws_sdk_sagemaker.types.query_lineage_types

        out["lineage_types"] = (
            aws_sdk_sagemaker.types.query_lineage_types.deserialize_aws_json_1_1(
                data["LineageTypes"]
            )
        )
    if "CreatedBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedBefore"]
            )
        )
    if "CreatedAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedAfter"]
            )
        )
    if "ModifiedBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["modified_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["ModifiedBefore"]
            )
        )
    if "ModifiedAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["modified_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["ModifiedAfter"]
            )
        )
    if "Properties" in data:
        import aws_sdk_sagemaker.types.query_properties

        out["properties"] = (
            aws_sdk_sagemaker.types.query_properties.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    return out
