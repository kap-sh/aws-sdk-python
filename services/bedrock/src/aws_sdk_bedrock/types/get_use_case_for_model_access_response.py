"""Generated from Smithy shape ``com.amazonaws.bedrock#GetUseCaseForModelAccessResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.acknowledgement_form_data_body


class GetUseCaseForModelAccessResponse(TypedDict):
    form_data: "aws_sdk_bedrock.types.acknowledgement_form_data_body.AcknowledgementFormDataBody"
    """<p>Get customer profile Response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUseCaseForModelAccessResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.acknowledgement_form_data_body

    out["formData"] = (
        aws_sdk_bedrock.types.acknowledgement_form_data_body.serialize_json(
            value["form_data"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetUseCaseForModelAccessResponse:
    out: GetUseCaseForModelAccessResponse = {}  # type: ignore[typeddict-item]
    if "formData" in data:
        import aws_sdk_bedrock.types.acknowledgement_form_data_body

        out["form_data"] = (
            aws_sdk_bedrock.types.acknowledgement_form_data_body.deserialize_json(
                data["formData"]
            )
        )
    else:
        raise DeserializationError(
            "GetUseCaseForModelAccessResponse.form_data required"
        )
    return out
