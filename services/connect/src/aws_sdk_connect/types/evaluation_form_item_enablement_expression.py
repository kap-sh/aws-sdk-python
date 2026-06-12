"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementExpression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_item_enablement_source
    import aws_sdk_connect.types.evaluation_form_item_enablement_source_value_list
    import aws_sdk_connect.types.evaluation_form_item_source_values_comparator


class EvaluationFormItemEnablementExpression(TypedDict):
    source: "aws_sdk_connect.types.evaluation_form_item_enablement_source.EvaluationFormItemEnablementSource"
    """<p>A source item of enablement expression.</p>"""
    values: "aws_sdk_connect.types.evaluation_form_item_enablement_source_value_list.EvaluationFormItemEnablementSourceValueList"
    """<p>A list of values from source item.</p>"""
    comparator: "aws_sdk_connect.types.evaluation_form_item_source_values_comparator.EvaluationFormItemSourceValuesComparator"
    """<p>A comparator to be used against list of values. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementExpression) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.evaluation_form_item_enablement_source

    out["Source"] = (
        aws_sdk_connect.types.evaluation_form_item_enablement_source.serialize_json(
            value["source"]
        )
    )
    import aws_sdk_connect.types.evaluation_form_item_enablement_source_value_list

    out["Values"] = (
        aws_sdk_connect.types.evaluation_form_item_enablement_source_value_list.serialize_json(
            value["values"]
        )
    )
    import aws_sdk_connect.types.evaluation_form_item_source_values_comparator

    out["Comparator"] = (
        aws_sdk_connect.types.evaluation_form_item_source_values_comparator.serialize_json(
            value["comparator"]
        )
    )
    return out


def deserialize_json(data: dict) -> EvaluationFormItemEnablementExpression:
    out: EvaluationFormItemEnablementExpression = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        import aws_sdk_connect.types.evaluation_form_item_enablement_source

        out["source"] = (
            aws_sdk_connect.types.evaluation_form_item_enablement_source.deserialize_json(
                data["Source"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationFormItemEnablementExpression.source required"
        )
    if "Values" in data:
        import aws_sdk_connect.types.evaluation_form_item_enablement_source_value_list

        out["values"] = (
            aws_sdk_connect.types.evaluation_form_item_enablement_source_value_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationFormItemEnablementExpression.values required"
        )
    if "Comparator" in data:
        import aws_sdk_connect.types.evaluation_form_item_source_values_comparator

        out["comparator"] = (
            aws_sdk_connect.types.evaluation_form_item_source_values_comparator.deserialize_json(
                data["Comparator"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationFormItemEnablementExpression.comparator required"
        )
    return out
