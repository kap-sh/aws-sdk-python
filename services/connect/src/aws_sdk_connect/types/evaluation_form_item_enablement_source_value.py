"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementSourceValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_item_enablement_source_value_type
    import aws_sdk_connect.types.reference_id


class EvaluationFormItemEnablementSourceValue(TypedDict):
    type: "aws_sdk_connect.types.evaluation_form_item_enablement_source_value_type.EvaluationFormItemEnablementSourceValueType"
    """<p>A type of source item value. </p>"""
    ref_id: NotRequired["aws_sdk_connect.types.reference_id.ReferenceId"]
    """<p>A referenceId of the source value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementSourceValue) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.evaluation_form_item_enablement_source_value_type

    out["Type"] = (
        aws_sdk_connect.types.evaluation_form_item_enablement_source_value_type.serialize_json(
            value["type"]
        )
    )
    if "ref_id" in value:
        out["RefId"] = value["ref_id"]
    return out


def deserialize_json(data: dict) -> EvaluationFormItemEnablementSourceValue:
    out: EvaluationFormItemEnablementSourceValue = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_connect.types.evaluation_form_item_enablement_source_value_type

        out["type"] = (
            aws_sdk_connect.types.evaluation_form_item_enablement_source_value_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationFormItemEnablementSourceValue.type required"
        )
    if "RefId" in data:
        out["ref_id"] = data["RefId"]
    return out
