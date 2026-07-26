"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.compliance_query_operator_type
    import capo_ssm.types.compliance_string_filter_key
    import capo_ssm.types.compliance_string_filter_value_list


class ComplianceStringFilter(TypedDict, closed=True):
    key: NotRequired[
        "capo_ssm.types.compliance_string_filter_key.ComplianceStringFilterKey"
    ]
    """<p>The name of the filter.</p>"""
    values: NotRequired[
        "capo_ssm.types.compliance_string_filter_value_list.ComplianceStringFilterValueList"
    ]
    """<p>The value for which to search.</p>"""
    type: NotRequired[
        "capo_ssm.types.compliance_query_operator_type.ComplianceQueryOperatorType"
    ]
    """<p>The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceStringFilter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import capo_ssm.types.compliance_string_filter_value_list

        out["Values"] = (
            capo_ssm.types.compliance_string_filter_value_list.serialize_aws_json_1_1(
                value["values"]
            )
        )
    if "type" in value:
        import capo_ssm.types.compliance_query_operator_type

        out["Type"] = (
            capo_ssm.types.compliance_query_operator_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceStringFilter:
    out: ComplianceStringFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Values" in data:
        import capo_ssm.types.compliance_string_filter_value_list

        out["values"] = (
            capo_ssm.types.compliance_string_filter_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    if "Type" in data:
        import capo_ssm.types.compliance_query_operator_type

        out["type"] = (
            capo_ssm.types.compliance_query_operator_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    return out
