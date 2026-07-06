"""Generated from Smithy shape ``com.amazonaws.glue#StatisticSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_name_list
    import aws_sdk_glue.types.double
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.reference_datasets_list
    import aws_sdk_glue.types.run_identifier
    import aws_sdk_glue.types.statistic_evaluation_level
    import aws_sdk_glue.types.statistic_name_string
    import aws_sdk_glue.types.statistic_properties_map
    import aws_sdk_glue.types.timestamp
    import aws_sdk_glue.types.timestamped_inclusion_annotation


class StatisticSummary(TypedDict, closed=True):
    statistic_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The Statistic ID.</p>"""
    profile_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The Profile ID.</p>"""
    run_identifier: NotRequired["aws_sdk_glue.types.run_identifier.RunIdentifier"]
    """<p>The Run Identifier</p>"""
    statistic_name: NotRequired[
        "aws_sdk_glue.types.statistic_name_string.StatisticNameString"
    ]
    """<p>The name of the statistic.</p>"""
    double_value: "aws_sdk_glue.types.double.Double"
    """<p>The value of the statistic.</p>"""
    evaluation_level: NotRequired[
        "aws_sdk_glue.types.statistic_evaluation_level.StatisticEvaluationLevel"
    ]
    """<p>The evaluation level of the statistic. Possible values: <code>Dataset</code>, <code>Column</code>, <code>Multicolumn</code>.</p>"""
    columns_referenced: NotRequired[
        "aws_sdk_glue.types.column_name_list.ColumnNameList"
    ]
    """<p>The list of columns referenced by the statistic.</p>"""
    referenced_datasets: NotRequired[
        "aws_sdk_glue.types.reference_datasets_list.ReferenceDatasetsList"
    ]
    """<p>The list of datasets referenced by the statistic.</p>"""
    statistic_properties: NotRequired[
        "aws_sdk_glue.types.statistic_properties_map.StatisticPropertiesMap"
    ]
    """<p>A <code>StatisticPropertiesMap</code>, which contains a <code>NameString</code> and <code>DescriptionString</code> </p>"""
    recorded_on: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The timestamp when the statistic was recorded.</p>"""
    inclusion_annotation: NotRequired[
        "aws_sdk_glue.types.timestamped_inclusion_annotation.TimestampedInclusionAnnotation"
    ]
    """<p>The inclusion annotation for the statistic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatisticSummary) -> dict:
    out: dict = {}
    if "statistic_id" in value:
        out["StatisticId"] = value["statistic_id"]
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "run_identifier" in value:
        import aws_sdk_glue.types.run_identifier

        out["RunIdentifier"] = aws_sdk_glue.types.run_identifier.serialize_aws_json_1_1(
            value["run_identifier"]
        )
    if "statistic_name" in value:
        out["StatisticName"] = value["statistic_name"]
    out["DoubleValue"] = value.get("double_value", 0)
    if "evaluation_level" in value:
        import aws_sdk_glue.types.statistic_evaluation_level

        out["EvaluationLevel"] = (
            aws_sdk_glue.types.statistic_evaluation_level.serialize_aws_json_1_1(
                value["evaluation_level"]
            )
        )
    if "columns_referenced" in value:
        import aws_sdk_glue.types.column_name_list

        out["ColumnsReferenced"] = (
            aws_sdk_glue.types.column_name_list.serialize_aws_json_1_1(
                value["columns_referenced"]
            )
        )
    if "referenced_datasets" in value:
        import aws_sdk_glue.types.reference_datasets_list

        out["ReferencedDatasets"] = (
            aws_sdk_glue.types.reference_datasets_list.serialize_aws_json_1_1(
                value["referenced_datasets"]
            )
        )
    if "statistic_properties" in value:
        import aws_sdk_glue.types.statistic_properties_map

        out["StatisticProperties"] = (
            aws_sdk_glue.types.statistic_properties_map.serialize_aws_json_1_1(
                value["statistic_properties"]
            )
        )
    if "recorded_on" in value:
        import aws_sdk_glue.types.timestamp

        out["RecordedOn"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["recorded_on"]
        )
    if "inclusion_annotation" in value:
        import aws_sdk_glue.types.timestamped_inclusion_annotation

        out["InclusionAnnotation"] = (
            aws_sdk_glue.types.timestamped_inclusion_annotation.serialize_aws_json_1_1(
                value["inclusion_annotation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StatisticSummary:
    out: StatisticSummary = {}  # type: ignore[typeddict-item]
    if "StatisticId" in data:
        out["statistic_id"] = data["StatisticId"]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    if "RunIdentifier" in data:
        import aws_sdk_glue.types.run_identifier

        out["run_identifier"] = (
            aws_sdk_glue.types.run_identifier.deserialize_aws_json_1_1(
                data["RunIdentifier"]
            )
        )
    if "StatisticName" in data:
        out["statistic_name"] = data["StatisticName"]
    if "DoubleValue" in data:
        out["double_value"] = data["DoubleValue"]
    else:
        out["double_value"] = 0
    if "EvaluationLevel" in data:
        import aws_sdk_glue.types.statistic_evaluation_level

        out["evaluation_level"] = (
            aws_sdk_glue.types.statistic_evaluation_level.deserialize_aws_json_1_1(
                data["EvaluationLevel"]
            )
        )
    if "ColumnsReferenced" in data:
        import aws_sdk_glue.types.column_name_list

        out["columns_referenced"] = (
            aws_sdk_glue.types.column_name_list.deserialize_aws_json_1_1(
                data["ColumnsReferenced"]
            )
        )
    if "ReferencedDatasets" in data:
        import aws_sdk_glue.types.reference_datasets_list

        out["referenced_datasets"] = (
            aws_sdk_glue.types.reference_datasets_list.deserialize_aws_json_1_1(
                data["ReferencedDatasets"]
            )
        )
    if "StatisticProperties" in data:
        import aws_sdk_glue.types.statistic_properties_map

        out["statistic_properties"] = (
            aws_sdk_glue.types.statistic_properties_map.deserialize_aws_json_1_1(
                data["StatisticProperties"]
            )
        )
    if "RecordedOn" in data:
        import aws_sdk_glue.types.timestamp

        out["recorded_on"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["RecordedOn"]
        )
    if "InclusionAnnotation" in data:
        import aws_sdk_glue.types.timestamped_inclusion_annotation

        out["inclusion_annotation"] = (
            aws_sdk_glue.types.timestamped_inclusion_annotation.deserialize_aws_json_1_1(
                data["InclusionAnnotation"]
            )
        )
    return out
