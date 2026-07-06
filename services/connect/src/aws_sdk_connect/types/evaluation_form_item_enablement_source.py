"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_item_enablement_source_type
    import aws_sdk_connect.types.reference_id


class EvaluationFormItemEnablementSource(TypedDict, closed=True):
    type: "aws_sdk_connect.types.evaluation_form_item_enablement_source_type.EvaluationFormItemEnablementSourceType"
    """<p>A type of source item. </p>"""
    ref_id: NotRequired["aws_sdk_connect.types.reference_id.ReferenceId"]
    """<p>A referenceId of the source item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementSource) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.evaluation_form_item_enablement_source_type

    out["Type"] = (
        aws_sdk_connect.types.evaluation_form_item_enablement_source_type.serialize_json(
            value["type"]
        )
    )
    if "ref_id" in value:
        out["RefId"] = value["ref_id"]
    return out


def deserialize_json(data: dict) -> EvaluationFormItemEnablementSource:
    out: EvaluationFormItemEnablementSource = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_connect.types.evaluation_form_item_enablement_source_type

        out["type"] = (
            aws_sdk_connect.types.evaluation_form_item_enablement_source_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("EvaluationFormItemEnablementSource.type required")
    if "RefId" in data:
        out["ref_id"] = data["RefId"]
    return out
