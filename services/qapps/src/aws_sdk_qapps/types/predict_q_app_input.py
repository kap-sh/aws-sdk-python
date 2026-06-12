"""Generated from Smithy shape ``com.amazonaws.qapps#PredictQAppInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.predict_q_app_input_options


class PredictQAppInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    options: NotRequired[
        "aws_sdk_qapps.types.predict_q_app_input_options.PredictQAppInputOptions"
    ]
    """<p>The input to generate the Q App definition from, either a conversation or problem statement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredictQAppInput) -> dict:
    out: dict = {}
    if "options" in value:
        import aws_sdk_qapps.types.predict_q_app_input_options

        out["options"] = aws_sdk_qapps.types.predict_q_app_input_options.serialize_json(
            value["options"]
        )
    return out


def deserialize_json(data: dict) -> PredictQAppInput:
    out: PredictQAppInput = {}  # type: ignore[typeddict-item]
    if "options" in data:
        import aws_sdk_qapps.types.predict_q_app_input_options

        out["options"] = (
            aws_sdk_qapps.types.predict_q_app_input_options.deserialize_json(
                data["options"]
            )
        )
    return out
