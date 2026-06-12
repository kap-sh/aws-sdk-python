"""Generated from Smithy shape ``com.amazonaws.databrew#Rule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.column_selector_list
    import aws_sdk_databrew.types.disabled
    import aws_sdk_databrew.types.expression
    import aws_sdk_databrew.types.rule_name
    import aws_sdk_databrew.types.threshold
    import aws_sdk_databrew.types.values_map


class Rule(TypedDict):
    name: "aws_sdk_databrew.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    disabled: "aws_sdk_databrew.types.disabled.Disabled"
    """<p>A value that specifies whether the rule is disabled. Once a rule is disabled, a profile job will not validate it during a job run. Default value is false.</p>"""
    check_expression: "aws_sdk_databrew.types.expression.Expression"
    """<p>The expression which includes column references, condition names followed by variable references, possibly grouped and combined with other conditions. For example, <code>(:col1 starts_with :prefix1 or :col1 starts_with :prefix2) and (:col1 ends_with :suffix1 or :col1 ends_with :suffix2)</code>. Column and value references are substitution variables that should start with the ':' symbol. Depending on the context, substitution variables' values can be either an actual value or a column name. These values are defined in the SubstitutionMap. If a CheckExpression starts with a column reference, then ColumnSelectors in the rule should be null. If ColumnSelectors has been defined, then there should be no column reference in the left side of a condition, for example, <code>is_between :val1 and :val2</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/databrew/latest/dg/profile.data-quality-available-checks.html\">Available checks</a> </p>"""
    substitution_map: NotRequired["aws_sdk_databrew.types.values_map.ValuesMap"]
    """<p>The map of substitution variable names to their values used in a check expression. Variable names should start with a ':' (colon). Variable values can either be actual values or column names. To differentiate between the two, column names should be enclosed in backticks, for example, <code>\":col1\": \"`Column A`\".</code> </p>"""
    threshold: NotRequired["aws_sdk_databrew.types.threshold.Threshold"]
    """<p>The threshold used with a non-aggregate check expression. Non-aggregate check expressions will be applied to each row in a specific column, and the threshold will be used to determine whether the validation succeeds.</p>"""
    column_selectors: NotRequired[
        "aws_sdk_databrew.types.column_selector_list.ColumnSelectorList"
    ]
    """<p>List of column selectors. Selectors can be used to select columns using a name or regular expression from the dataset. Rule will be applied to selected columns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Rule) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Disabled"] = value.get("disabled", False)
    out["CheckExpression"] = value["check_expression"]
    if "substitution_map" in value:
        import aws_sdk_databrew.types.values_map

        out["SubstitutionMap"] = aws_sdk_databrew.types.values_map.serialize_json(
            value["substitution_map"]
        )
    if "threshold" in value:
        import aws_sdk_databrew.types.threshold

        out["Threshold"] = aws_sdk_databrew.types.threshold.serialize_json(
            value["threshold"]
        )
    if "column_selectors" in value:
        import aws_sdk_databrew.types.column_selector_list

        out["ColumnSelectors"] = (
            aws_sdk_databrew.types.column_selector_list.serialize_json(
                value["column_selectors"]
            )
        )
    return out


def deserialize_json(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Rule.name required")
    if "Disabled" in data:
        out["disabled"] = data["Disabled"]
    else:
        out["disabled"] = False
    if "CheckExpression" in data:
        out["check_expression"] = data["CheckExpression"]
    else:
        raise DeserializationError("Rule.check_expression required")
    if "SubstitutionMap" in data:
        import aws_sdk_databrew.types.values_map

        out["substitution_map"] = aws_sdk_databrew.types.values_map.deserialize_json(
            data["SubstitutionMap"]
        )
    if "Threshold" in data:
        import aws_sdk_databrew.types.threshold

        out["threshold"] = aws_sdk_databrew.types.threshold.deserialize_json(
            data["Threshold"]
        )
    if "ColumnSelectors" in data:
        import aws_sdk_databrew.types.column_selector_list

        out["column_selectors"] = (
            aws_sdk_databrew.types.column_selector_list.deserialize_json(
                data["ColumnSelectors"]
            )
        )
    return out
