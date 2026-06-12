"""Generated from Smithy shape ``com.amazonaws.qapps#FormInputCardInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.card_type
    import aws_sdk_qapps.types.form_input_card_metadata
    import aws_sdk_qapps.types.input_card_compute_mode
    import aws_sdk_qapps.types.title
    import aws_sdk_qapps.types.uuid


class FormInputCardInput(TypedDict):
    title: "aws_sdk_qapps.types.title.Title"
    """<p>The title or label of the form input card.</p>"""
    id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the form input card.</p>"""
    type: "aws_sdk_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    metadata: "aws_sdk_qapps.types.form_input_card_metadata.FormInputCardMetadata"
    """<p>The metadata that defines the form input card data.</p>"""
    compute_mode: NotRequired[
        "aws_sdk_qapps.types.input_card_compute_mode.InputCardComputeMode"
    ]
    """<p>The compute mode of the form input card. This property determines whether individual participants of a data collection session can submit multiple response or one response. A compute mode of <code>append</code> shall allow participants to submit the same form multiple times with different values. A compute mode of <code>replace</code>code&gt; shall overwrite the current value for each participant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormInputCardInput) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["id"] = value["id"]
    import aws_sdk_qapps.types.card_type

    out["type"] = aws_sdk_qapps.types.card_type.serialize_json(
        value.get("type", "form-input")
    )
    import aws_sdk_qapps.types.form_input_card_metadata

    out["metadata"] = aws_sdk_qapps.types.form_input_card_metadata.serialize_json(
        value["metadata"]
    )
    if "compute_mode" in value:
        import aws_sdk_qapps.types.input_card_compute_mode

        out["computeMode"] = aws_sdk_qapps.types.input_card_compute_mode.serialize_json(
            value["compute_mode"]
        )
    return out


def deserialize_json(data: dict) -> FormInputCardInput:
    out: FormInputCardInput = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("FormInputCardInput.title required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FormInputCardInput.id required")
    if "type" in data:
        import aws_sdk_qapps.types.card_type

        out["type"] = aws_sdk_qapps.types.card_type.deserialize_json(data["type"])
    else:
        out["type"] = "form-input"
    if "metadata" in data:
        import aws_sdk_qapps.types.form_input_card_metadata

        out["metadata"] = aws_sdk_qapps.types.form_input_card_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("FormInputCardInput.metadata required")
    if "computeMode" in data:
        import aws_sdk_qapps.types.input_card_compute_mode

        out["compute_mode"] = (
            aws_sdk_qapps.types.input_card_compute_mode.deserialize_json(
                data["computeMode"]
            )
        )
    return out
